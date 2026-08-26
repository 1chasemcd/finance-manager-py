from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import DatabaseSessionManager

sessionmanager = DatabaseSessionManager()


async def get_db_session() -> AsyncGenerator[AsyncSession]:
    async with sessionmanager.session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db_session)]
