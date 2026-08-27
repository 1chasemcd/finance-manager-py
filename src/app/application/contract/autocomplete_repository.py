from typing import Protocol

from app.core.result import Result
from app.schemas.common import AutocompleteEntry, AutocompleteRequest


class AutocompleteRepository(Protocol):
    async def search(
        self, name: str, request: AutocompleteRequest
    ) -> Result[list[AutocompleteEntry]]: ...
    async def single(self, name: str, id: int) -> Result[AutocompleteEntry]: ...
