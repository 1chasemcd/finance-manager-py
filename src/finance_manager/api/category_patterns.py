from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from finance_manager.core.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.category_patterns import CategoryPatternRepositoryDep
from finance_manager.schemas.category_pattern import CategoryPatternResponse, WriteCategoryPattern

router = APIRouter(prefix="/categorypatterns")


@router.get(
    "/{id}",
    response_model=CategoryPatternResponse,
    responses=handled_error_responses(),
)
async def lookup_category_pattern(
    id: int,
    repo: CategoryPatternRepositoryDep,
) -> CategoryPatternResponse | JSONResponse:
    result = await repo.lookup(id)
    return handle_result(result)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses=handled_error_responses(),
)
async def create_category_pattern(
    request: WriteCategoryPattern,
    repo: CategoryPatternRepositoryDep,
) -> None | JSONResponse:
    result = await repo.create(request)
    return handle_result(result)


@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def update_category_pattern(
    id: int,
    request: WriteCategoryPattern,
    repo: CategoryPatternRepositoryDep,
) -> None | JSONResponse:
    result = await repo.update(id, request)
    return handle_result(result)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def delete_category_pattern(
    id: int,
    repo: CategoryPatternRepositoryDep,
) -> None | JSONResponse:
    result = await repo.delete(id)
    return handle_result(result)
