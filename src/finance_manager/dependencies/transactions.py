from typing import Annotated

from fastapi import Depends

from finance_manager.application.contract.transaction_repository import TransactionRepository
from finance_manager.dependencies.database import SessionDep
from finance_manager.infrastructure.repositories.transaction_repository import (
    TransactionRepositoryImpl,
)


def get_transaction_repository(
    session: SessionDep,
) -> TransactionRepository:
    return TransactionRepositoryImpl(session)


TransactionRepositoryDep = Annotated[
    TransactionRepository,
    Depends(get_transaction_repository),
]
