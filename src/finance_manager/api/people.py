# app/api/v1/users.py
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from finance_manager.core.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.people import PersonCommandServiceDep, PersonQueryServiceDep
from finance_manager.schemas.person import PersonResponse, WritePerson

router = APIRouter(prefix="/people")


@router.get(
    "/{id}",
    response_model=PersonResponse,
    responses=handled_error_responses(),
)
async def lookup_person(
    id: int,
    service: PersonQueryServiceDep,
) -> PersonResponse | JSONResponse:
    result = await service.lookup(id)
    return handle_result(result)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses=handled_error_responses(),
)
async def create_person(
    request: WritePerson,
    service: PersonCommandServiceDep,
) -> None | JSONResponse:
    result = await service.create(request)
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
    service: PersonCommandServiceDep,
) -> None | JSONResponse:
    result = await service.update(id, request)
    return handle_result(result)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def delete_person(
    id: int,
    service: PersonCommandServiceDep,
) -> None | JSONResponse:
    result = await service.delete(id)
    return handle_result(result)
