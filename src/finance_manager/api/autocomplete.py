from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from finance_manager.core.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.people import PersonAutocompleteRepositoryDep
from finance_manager.schemas.common import PagedRequest

AutocompleteResponse = dict[int, str]

router = APIRouter(prefix="/autocomplete")


@router.get(
    "/person",
    response_model=AutocompleteResponse,
    responses=handled_error_responses(),
)
async def search_person(
    request: Annotated[PagedRequest, Query()],
    repo: PersonAutocompleteRepositoryDep,
) -> AutocompleteResponse | JSONResponse:
    result = await repo.search(request)
    return handle_result(result)


@router.get(
    "/person/{id}",
    response_model=str,
    responses=handled_error_responses(),
)
async def single_person(
    id: int,
    repo: PersonAutocompleteRepositoryDep,
) -> str | JSONResponse:
    result = await repo.single(id)
    return handle_result(result)
