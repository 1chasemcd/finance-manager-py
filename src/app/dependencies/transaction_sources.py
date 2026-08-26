from typing import Annotated

from fastapi import Depends

from app.application.contract.transaction_source_repository import (
    TransactionSourceRepository,
)
from app.dependencies.database import SessionDep
from app.infrastructure.repositories.transaction_source_repository import (
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
