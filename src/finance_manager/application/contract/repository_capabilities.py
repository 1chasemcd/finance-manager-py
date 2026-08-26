from typing import Protocol

from finance_manager.core import Result
from finance_manager.schemas.common import PagedQuery, SearchResponse


class LookupHandler[TModel](Protocol):
    async def lookup(self, id: int) -> Result[TModel]: ...


class SearchHandler[
    TModel,
    TSearch = PagedQuery,
](Protocol):
    async def search(self, request: TSearch) -> Result[SearchResponse[TModel]]: ...


class CreateHandler[TCreate](Protocol):
    async def create(self, request: TCreate) -> Result: ...


class UpdateHandler[TUpdate](Protocol):
    async def update(self, id: int, request: TUpdate) -> Result: ...


class DeleteHandler(Protocol):
    async def delete(self, id: int) -> Result: ...
