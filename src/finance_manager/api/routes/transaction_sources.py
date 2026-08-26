from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from finance_manager.api.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.transaction_sources import TransactionSourceRepositoryDep
from finance_manager.schemas.common import PagedQuery
from finance_manager.schemas.transaction_source import (
    TransactionSource,
    WriteTransactionSource,
)

router = APIRouter(prefix="/transactionsources")


@router.get(
    "/{id}",
    response_model=TransactionSource,
    responses=handled_error_responses(),
)
async def lookup_transaction_source(
    id: int,
    repo: TransactionSourceRepositoryDep,
) -> TransactionSource | JSONResponse:
    result = await repo.lookup(id)
    return handle_result(result)


@router.get(
    "/",
    response_model=list[TransactionSource],
    responses=handled_error_responses(),
)
async def search_transaction_sources(
    request: Annotated[PagedQuery, Query()],
    repo: TransactionSourceRepositoryDep,
) -> list[TransactionSource] | JSONResponse:
    result = await repo.search(request)
    return handle_result(result)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=None,
    responses=handled_error_responses(),
)
async def create_transaction_source(
    request: WriteTransactionSource,
    repo: TransactionSourceRepositoryDep,
) -> None | JSONResponse:
    result = await repo.create(request)
    return handle_result(result)


@router.put(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def update_transaction_source(
    id: int,
    request: WriteTransactionSource,
    repo: TransactionSourceRepositoryDep,
) -> None | JSONResponse:
    result = await repo.update(id, request)
    return handle_result(result)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses=handled_error_responses(),
)
async def delete_transaction_source(
    id: int,
    repo: TransactionSourceRepositoryDep,
) -> None | JSONResponse:
    result = await repo.delete(id)
    return handle_result(result)
