import sqlite3
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

from sqlalchemy import StaticPool, event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.config import Settings
from app.infrastructure import seed
from app.infrastructure.models.db_base import DbBase


class DatabaseSessionManager:
    def __init__(self) -> None:
        self._engine = None
        self._sessionmaker = None

    async def init(self, config: Settings) -> None:
        db_args: dict[str, Any] = {
            "pool_pre_ping": True,
            "echo": False,
            "pool_size": config.database_pool_size,
            "max_overflow": config.database_max_overflow,
        }

        if config.app_env != "prod":
            db_args["poolclass"] = StaticPool
            db_args["connect_args"] = {"check_same_thread": False}
            db_args.pop("pool_size")
            db_args.pop("max_overflow")

        self._engine = create_async_engine(config.database_url, **db_args)

        # enable foreign key constraints
        @event.listens_for(self._engine.sync_engine, "connect")
        def _set_sqlite_pragma(
            dbapi_connection: sqlite3.Connection,
            connection_record: Any,
        ) -> None:
            dbapi_connection.execute("PRAGMA foreign_keys=ON")

        self._sessionmaker = async_sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

        if config.app_env != "prod":
            async with self._engine.connect() as connection:
                await connection.run_sync(DbBase.metadata.create_all)

            if config.database_seed_data is not None:
                async with self.session() as session:
                    await seed.create_data(session, config.database_seed_data)

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
