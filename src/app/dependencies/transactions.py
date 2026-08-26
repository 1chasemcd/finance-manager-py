from typing import Annotated

from fastapi import Depends

from app.application.contract.transaction_repository import TransactionRepository
from app.dependencies.database import SessionDep
from app.infrastructure.repositories.transaction_repository import (
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
