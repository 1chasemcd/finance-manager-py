from abc import ABC, abstractmethod

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.core.errors import NotFound
from finance_manager.core.result import Ok, Result
from finance_manager.schemas.common import PagedRequest


class AutocompleteRepository[T: PagedRequest = PagedRequest](ABC):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def search(self, request: T) -> Result[dict[int, str]]:
        stmt = self._statement().offset(request.skip).limit(request.take)
        stmt = self._filter(stmt)
        res = await self._session.execute(stmt)
        pairs: dict[int, str] = {key: value for key, value in res}
        return Ok(pairs)

    async def single(self, id: int) -> Result[str]:
        stmt = self._statement()
        id_column = stmt.selected_columns[0]
        stmt = stmt.where(id_column == id)
        res = await self._session.execute(stmt)
        single = res.one_or_none()
        if not single:
            return NotFound()
        return Ok(single.tuple()[1])

    @abstractmethod
    def _statement(self) -> Select[tuple[int, str]]:
        pass

    def _filter(self, stmt: Select[tuple[int, str]]) -> Select[tuple[int, str]]:
        return stmt
