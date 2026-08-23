from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from finance_manager.core.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.transactions import TransactionRepositoryDep
from finance_manager.schemas.transaction import TransactionResponse, WriteTransaction

router = APIRouter(prefix="/transactions")


@router.get(
    "/{id}",
    response_model=TransactionResponse,
    responses=handled_error_responses(),
)
async def lookup_transaction(
    id: int,
    repo: TransactionRepositoryDep,
) -> TransactionResponse | JSONResponse:
    result = await repo.lookup(id)
    return handle_result(result)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses=handled_error_responses(),
)
async def create_transaction(
    request: WriteTransaction,
    repo: TransactionRepositoryDep,
) -> None | JSONResponse:
    result = await repo.create(request)
    return handle_result(result)


@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def update_transaction(
    id: int,
    request: WriteTransaction,
    repo: TransactionRepositoryDep,
) -> None | JSONResponse:
    result = await repo.update(id, request)
    return handle_result(result)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def delete_transaction(
    id: int,
    repo: TransactionRepositoryDep,
) -> None | JSONResponse:
    result = await repo.delete(id)
    return handle_result(result)
