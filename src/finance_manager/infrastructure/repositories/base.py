from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.core import NoContent, NotFound, Ok, Result
from finance_manager.infrastructure.models import DbBase
from finance_manager.schemas.common import HasPage, PagedQuery

SelectStatement = Select[tuple[Any, ...]]


class BaseRepository[
    ModelType: DbBase,
    ReadType: BaseModel,
    CreateType: BaseModel,
    UpdateType = CreateType,
    SearchType: HasPage = PagedQuery,
](ABC):
    def __init__(
        self,
        model: type[ModelType],
        readType: type[ReadType],
        session: AsyncSession,
    ) -> None:
        self.model = model
        self.readType = readType
        self.session = session

    @abstractmethod
    def _select_statement(self) -> SelectStatement:
        pass

    @abstractmethod
    def _map_create(self, request: CreateType) -> ModelType:
        pass

    @abstractmethod
    def _map_update(self, request: UpdateType, model: ModelType) -> None:
        pass

    def _filter_search(self, statement: SelectStatement, request: SearchType) -> SelectStatement:
        return statement.order_by(self.model.id).offset(request.skip).limit(request.take)

    async def lookup(self, id: int) -> Result[ReadType]:
        stmt = self._select_statement()
        res = (
            (await self.session.execute(stmt.where(self.model.id == id).limit(2)))
            .mappings()
            .one_or_none()
        )
        if not res:
            return NotFound()
        read = self.readType.model_validate(res)
        return Ok(read)

    async def search(self, request: SearchType) -> Result[list[ReadType]]:
        stmt = self._select_statement()
        res = (await self.session.execute(self._filter_search(stmt, request))).mappings()
        return Ok([self.readType.model_validate(m) for m in res])

    async def update(self, id: int, request: UpdateType) -> Result:
        to_update = await self.session.get(self.model, id)
        if not to_update:
            return NotFound()
        self._map_update(request, to_update)
        await self.session.flush()
        return NoContent()

    async def create(self, request: CreateType) -> Result:
        model = self._map_create(request)
        self.session.add(model)
        await self.session.flush()
        return NoContent()

    async def delete(self, id: int) -> Result:
        to_delete = await self.session.get(self.model, id)
        if not to_delete:
            return NotFound()
        await self.session.delete(to_delete)
        await self.session.flush()
        return NoContent()
