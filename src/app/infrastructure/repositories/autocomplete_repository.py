from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import NotFound, Ok, Result
from app.infrastructure.autocomplete_registry import AutocompleteRegistry
from app.schemas.common import AutocompleteRequest


class AutocompleteRepositoryImpl:
    def __init__(self, session: AsyncSession, registry: AutocompleteRegistry) -> None:
        self._session = session
        self._registry = registry

    async def search(self, name: str, request: AutocompleteRequest) -> Result[dict[int, str]]:
        entry = self._registry.get(name)
        if entry.status == "err":
            return entry
        search = f"%{request.search}%"
        stmt = (
            select(entry.value.id, entry.value.display)
            .where(entry.value.display.ilike(search))
            .offset(request.skip)
            .limit(request.take)
        )
        res = await self._session.execute(stmt)
        pairs: dict[int, str] = {key: value for key, value in res}
        return Ok(pairs)

    async def single(self, name: str, id: int) -> Result[str]:
        entry = self._registry.get(name)
        if entry.status == "err":
            return entry
        stmt = select(entry.value.display).where(entry.value.id == id)
        res = await self._session.scalar(stmt)
        if not res:
            return NotFound()
        return Ok(res)
