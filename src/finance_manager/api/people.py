# app/api/v1/users.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from finance_manager.core.result_handler import handle_result
from finance_manager.dependencies.people import PersonQueryServiceDep
from finance_manager.schemas.person import PersonResponse

router = APIRouter(prefix="/people")


@router.get("/{id}", response_model=PersonResponse)
async def get_person(
    id: int,
    service: PersonQueryServiceDep,
) -> PersonResponse | JSONResponse:
    result = await service.lookup(id)
    return handle_result(result)
