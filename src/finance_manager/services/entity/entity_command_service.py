from typing import Protocol

from pydantic import BaseModel

from finance_manager.core import Result


class CommandRepository[T: BaseModel](Protocol):
    async def create(self, request: T) -> Result: ...
    async def update(self, id: int, request: T) -> Result: ...
    async def delete(self, id: int) -> Result: ...


class EntityCommandService[T: BaseModel]:
    def __init__(self, repository: CommandRepository[T]) -> None:
        self.repository = repository

    async def create(self, request: T) -> Result:
        return await self.repository.create(request)

    async def update(self, id: int, request: T) -> Result:
        return await self.repository.create(request)

    async def delete(self, id: int) -> Result:
        return await self.repository.delete(id)
