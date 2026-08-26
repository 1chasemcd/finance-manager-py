from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from finance_manager.api.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.people import PersonRepositoryDep
from finance_manager.schemas.common import PagedQuery, SearchResponse
from finance_manager.schemas.person import Person, WritePerson

router = APIRouter(prefix="/people")


@router.get(
    "/{id}",
    response_model=Person,
    responses=handled_error_responses(),
)
async def lookup_person(
    id: int,
    repo: PersonRepositoryDep,
) -> Person | JSONResponse:
    result = await repo.lookup(id)
    return handle_result(result)


@router.get(
    "/",
    response_model=SearchResponse[Person],
    responses=handled_error_responses(),
)
async def search_people(
    request: Annotated[PagedQuery, Query()],
    repo: PersonRepositoryDep,
) -> SearchResponse[Person] | JSONResponse:
    result = await repo.search(request)
    return handle_result(result)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses=handled_error_responses(),
)
async def create_person(
    request: WritePerson,
    repo: PersonRepositoryDep,
) -> None | JSONResponse:
    result = await repo.create(request)
    return handle_result(result)


@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def update_person(
    id: int,
    request: WritePerson,
    repo: PersonRepositoryDep,
) -> None | JSONResponse:
    result = await repo.update(id, request)
    return handle_result(result)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def delete_person(
    id: int,
    repo: PersonRepositoryDep,
) -> None | JSONResponse:
    result = await repo.delete(id)
    return handle_result(result)
