from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from finance_manager.api.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.transaction_categories import TransactionCategoryRepositoryDep
from finance_manager.schemas.common import PagedQuery
from finance_manager.schemas.transaction_category import (
    TransactionCategory,
    WriteTransactionCategory,
)

router = APIRouter(prefix="/transactioncategories")


@router.get(
    "/{id}",
    response_model=TransactionCategory,
    responses=handled_error_responses(),
)
async def lookup_transaction_category(
    id: int,
    repo: TransactionCategoryRepositoryDep,
) -> TransactionCategory | JSONResponse:
    result = await repo.lookup(id)
    return handle_result(result)


@router.get(
    "/",
    response_model=list[TransactionCategory],
    responses=handled_error_responses(),
)
async def search_transaction_categories(
    request: Annotated[PagedQuery, Query()],
    repo: TransactionCategoryRepositoryDep,
) -> list[TransactionCategory] | JSONResponse:
    result = await repo.search(request)
    return handle_result(result)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses=handled_error_responses(),
)
async def create_transaction_category(
    request: WriteTransactionCategory,
    repo: TransactionCategoryRepositoryDep,
) -> None | JSONResponse:
    result = await repo.create(request)
    return handle_result(result)


@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def update_transaction_category(
    id: int,
    request: WriteTransactionCategory,
    repo: TransactionCategoryRepositoryDep,
) -> None | JSONResponse:
    result = await repo.update(id, request)
    return handle_result(result)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def delete_transaction_category(
    id: int,
    repo: TransactionCategoryRepositoryDep,
) -> None | JSONResponse:
    result = await repo.delete(id)
    return handle_result(result)
