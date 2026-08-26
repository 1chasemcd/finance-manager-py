from typing import Protocol

from app.core.result import Result
from app.schemas.common import AutocompleteRequest


class AutocompleteRepository(Protocol):
    async def search(self, name: str, request: AutocompleteRequest) -> Result[dict[int, str]]: ...
    async def single(self, name: str, id: int) -> Result[str]: ...
