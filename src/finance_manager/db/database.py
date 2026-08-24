from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from finance_manager.config import Settings
from finance_manager.models import Base


class DatabaseSessionManager:
    def __init__(self) -> None:
        self._engine = None
        self._sessionmaker = None

    async def init(self, config: Settings) -> None:
        if config.debug and config.database_use_in_memory:
            self._engine = create_async_engine(
                config.database_url,
                pool_pre_ping=True,
                echo=False,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool,
            )
            async with self._engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        else:
            self._engine = create_async_engine(
                config.database_url,
                pool_size=config.database_pool_size,
                max_overflow=config.database_max_overflow,
                pool_pre_ping=True,
                echo=False,
            )

        self._sessionmaker = async_sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

        if config.debug and config.database_seed is not None:
            async with self.session() as session:
                await config.database_seed(session)

    async def close(self) -> None:
        if self._engine:
            await self._engine.dispose()

    @asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession]:
        if self._sessionmaker is None:
            raise RuntimeError("DatabaseSessionManager is not initialized")

        async with self._sessionmaker() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
