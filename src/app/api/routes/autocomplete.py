from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.api.result_handler import handle_result, handled_error_responses
from app.dependencies.autocomplete import AutocompleteRepositoryDep
from app.schemas.common import AutocompleteEntry, AutocompleteRequest

router = APIRouter(prefix="/autocomplete")


@router.get(
    "/{entity}",
    response_model=list[AutocompleteEntry],
    responses=handled_error_responses(),
)
async def autocomplete_search(
    entity: str,
    request: Annotated[AutocompleteRequest, Query()],
    repo: AutocompleteRepositoryDep,
) -> list[AutocompleteEntry] | JSONResponse:
    result = await repo.search(entity, request)
    return handle_result(result)


@router.get(
    "/{entity}/{id}",
    response_model=AutocompleteEntry,
    responses=handled_error_responses(),
)
async def autocomplete_single(
    entity: str,
    id: int,
    repo: AutocompleteRepositoryDep,
) -> AutocompleteEntry | JSONResponse:
    result = await repo.single(entity, id)
    return handle_result(result)
