from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import NotFound, Ok, Result
from app.infrastructure.autocomplete_registry import AutocompleteRegistry
from app.schemas.common import AutocompleteEntry, AutocompleteRequest


class AutocompleteRepositoryImpl:
    def __init__(self, session: AsyncSession, registry: AutocompleteRegistry) -> None:
        self._session = session
        self._registry = registry

    async def search(
        self, entity: str, request: AutocompleteRequest
    ) -> Result[list[AutocompleteEntry]]:
        entry = self._registry.get(entity)
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
        pairs = [AutocompleteEntry(id=key, label=value) for key, value in res]
        return Ok(pairs)

    async def single(self, entity: str, id: int) -> Result[AutocompleteEntry]:
        entry = self._registry.get(entity)
        if entry.status == "err":
            return entry
        stmt = select(entry.value.display).where(entry.value.id == id)
        res = await self._session.scalar(stmt)
        if not res:
            return NotFound()
        return Ok(AutocompleteEntry(id=id, label=res))
