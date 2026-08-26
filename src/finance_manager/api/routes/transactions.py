from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from finance_manager.api.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.transactions import TransactionRepositoryDep
from finance_manager.schemas.common import SearchResponse
from finance_manager.schemas.transaction import SearchTransactions, Transaction

router = APIRouter(prefix="/transactions")


@router.get(
    "/{id}",
    response_model=Transaction,
    responses=handled_error_responses(),
)
async def lookup_transaction(
    id: int,
    repo: TransactionRepositoryDep,
) -> Transaction | JSONResponse:
    result = await repo.lookup(id)
    return handle_result(result)


@router.get(
    "/",
    response_model=SearchResponse[Transaction],
    responses=handled_error_responses(),
)
async def search_transactions(
    request: Annotated[SearchTransactions, Query()],
    repo: TransactionRepositoryDep,
) -> SearchResponse[Transaction] | JSONResponse:
    result = await repo.search(request)
    return handle_result(result)
