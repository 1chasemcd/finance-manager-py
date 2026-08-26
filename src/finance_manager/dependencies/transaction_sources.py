from typing import Annotated

from fastapi import Depends

from finance_manager.dependencies import SessionDep
from finance_manager.infrastructure.repositories import TransactionSourceRepository


def get_transaction_source_repository(
    session: SessionDep,
) -> TransactionSourceRepository:
    return TransactionSourceRepository(session)


TransactionSourceRepositoryDep = Annotated[
    TransactionSourceRepository,
    Depends(get_transaction_source_repository),
]
