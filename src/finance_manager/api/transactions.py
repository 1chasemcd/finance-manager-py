from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from finance_manager.core.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.transactions import TransactionRepositoryDep
from finance_manager.schemas.transaction import SearchTransactions, TransactionResponse

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


@router.get(
    "/",
    response_model=list[TransactionResponse],
    responses=handled_error_responses(),
)
async def search_transactions(
    request: Annotated[SearchTransactions, Query()],
    repo: TransactionRepositoryDep,
) -> list[TransactionResponse] | JSONResponse:
    result = await repo.search(request)
    return handle_result(result)
