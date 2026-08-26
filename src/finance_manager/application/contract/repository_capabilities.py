from typing import Protocol

from finance_manager.core import Result
from finance_manager.schemas.common import SearchResponse


class LookupHandler[TModel](Protocol):
    async def lookup(self, id: int) -> Result[TModel]: ...


class SearchHandler[TSearch, TModel](Protocol):
    async def search(self, request: TSearch) -> Result[SearchResponse[TModel]]: ...


class CreateHandler[TCreate](Protocol):
    async def create(self, request: TCreate) -> Result: ...


class UpdateHandler[TUpdate](Protocol):
    async def create(self, id: int, request: TUpdate) -> Result: ...


class DeleteHandler(Protocol):
    async def create(self, id: int) -> Result: ...
