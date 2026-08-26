from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.api.result_handler import handle_result, handled_error_responses
from app.dependencies.autocomplete import AutocompleteRepositoryDep
from app.schemas.common import AutocompleteRequest

AutocompleteResponse = dict[int, str]

router = APIRouter(prefix="/autocomplete")


@router.get(
    "/{name}",
    response_model=AutocompleteResponse,
    responses=handled_error_responses(),
)
async def autocomplete_search(
    name: str,
    request: Annotated[AutocompleteRequest, Query()],
    repo: AutocompleteRepositoryDep,
) -> AutocompleteResponse | JSONResponse:
    result = await repo.search(name, request)
    return handle_result(result)


@router.get(
    "/{name}/{id}",
    response_model=str,
    responses=handled_error_responses(),
)
async def autocomplete_single(
    name: str,
    id: int,
    repo: AutocompleteRepositoryDep,
) -> str | JSONResponse:
    result = await repo.single(name, id)
    return handle_result(result)
