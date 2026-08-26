from typing import Annotated

from fastapi import Depends

from finance_manager.dependencies import SessionDep
from finance_manager.infrastructure.repositories import TransactionRepository


def get_transaction_repository(
    session: SessionDep,
) -> TransactionRepository:
    return TransactionRepository(session)


TransactionRepositoryDep = Annotated[
    TransactionRepository,
    Depends(get_transaction_repository),
]
