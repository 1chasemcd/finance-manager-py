from typing import Annotated

from fastapi import Depends

from finance_manager.application.contract.transaction_source_repository import (
    TransactionSourceRepository,
)
from finance_manager.dependencies import SessionDep
from finance_manager.infrastructure.repositories.transaction_source_repository import (
    TransactionSourceRepositoryImpl,
)


def get_transaction_source_repository(
    session: SessionDep,
) -> TransactionSourceRepository:
    return TransactionSourceRepositoryImpl(session)


TransactionSourceRepositoryDep = Annotated[
    TransactionSourceRepository,
    Depends(get_transaction_source_repository),
]
