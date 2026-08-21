from typing import Protocol

from pydantic import BaseModel

from finance_manager.core import Result


class QueryRepository[T: BaseModel](Protocol):
    async def lookup(self, id: int) -> Result[T]: ...
    async def search(self, skip: int, take: int) -> Result[list[T]]: ...


class EntityQueryService[T: BaseModel]:
    def __init__(self, repository: QueryRepository[T]) -> None:
        self.repository = repository

    async def lookup(self, id: int) -> Result[T]:
        return await self.repository.lookup(id)

    async def search(self, skip: int, take: int) -> Result[list[T]]:
        return await self.repository.search(skip, take)
