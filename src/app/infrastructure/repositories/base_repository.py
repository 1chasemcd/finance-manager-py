from typing import Any

from pydantic import BaseModel
from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import NoContent, NotFound, Ok, Result
from app.infrastructure.models.db_base import DbBase
from app.schemas.common import HasPage, PagedQuery, SearchResponse

SelectStatement = Select[tuple[Any, ...]]


class BaseRepository[
    TOrm: DbBase,
    TModel: BaseModel,
    TCreate: BaseModel,
    TUpdate: BaseModel = TCreate,
    TSearch: HasPage = PagedQuery,
]:
    def __init__(
        self,
        orm_type: type[TOrm],
        model_type: type[TModel],
        session: AsyncSession,
    ) -> None:
        self.orm_type = orm_type
        self.model_type = model_type
        self.session = session

    def _select(self) -> SelectStatement:
        return select(*self.orm_type.__table__.columns)

    def _new(self) -> TOrm:
        return self.orm_type()

    def _map_create(self, request: TCreate, orm_model: TOrm) -> None:
        self._map_write(request, orm_model)

    def _map_update(self, request: TUpdate, orm_model: TOrm) -> None:
        self._map_write(request, orm_model)

    def _map_write(self, request: TUpdate | TCreate, orm_model: TOrm) -> None:
        values = request.model_dump()
        for field_name, value in values.items():
            setattr(orm_model, field_name, value)

    def _filter_search(self, statement: SelectStatement, request: TSearch) -> SelectStatement:
        return statement.order_by(self.orm_type.id)

    async def lookup(self, id: int) -> Result[TModel]:
        stmt = self._select()
        res = (
            (await self.session.execute(stmt.where(self.orm_type.id == id).limit(2)))
            .mappings()
            .one_or_none()
        )
        if not res:
            return NotFound()
        read = self.model_type.model_validate(res)
        return Ok(read)

    async def search(self, request: TSearch) -> Result[SearchResponse[TModel]]:
        stmt = self._select()
        filtered_stmt = self._filter_search(stmt, request)
        count = await self.session.scalar(
            select(func.count()).select_from(filtered_stmt.subquery())
        )
        count = 0 if count is None else count
        res = (
            await self.session.execute(filtered_stmt.offset(request.skip).limit(request.take))
        ).mappings()
        return Ok(
            SearchResponse(total=count, result=[self.model_type.model_validate(m) for m in res])
        )

    async def update(self, id: int, request: TUpdate) -> Result:
        to_update = await self.session.get(self.orm_type, id)
        if not to_update:
            return NotFound()
        self._map_update(request, to_update)
        await self.session.flush()
        return NoContent()

    async def create(self, request: TCreate) -> Result:
        new = self._new()
        self._map_create(request, new)
        self.session.add(new)
        await self.session.flush()
        return NoContent()

    async def delete(self, id: int) -> Result:
        to_delete = await self.session.get(self.orm_type, id)
        if not to_delete:
            return NotFound()
        await self.session.delete(to_delete)
        await self.session.flush()
        return NoContent()
