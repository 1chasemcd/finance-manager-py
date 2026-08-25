from fastapi import APIRouter
from fastapi.responses import JSONResponse

from finance_manager.core.result_handler import handle_result, handled_error_responses
from finance_manager.dependencies.transactions import TransactionRepositoryDep
from finance_manager.schemas.transaction import TransactionResponse

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
