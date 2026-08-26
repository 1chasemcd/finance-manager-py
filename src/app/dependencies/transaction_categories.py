from typing import Annotated

from fastapi import Depends

from app.application.contract.transaction_category_repository import (
    TransactionCategoryRepository,
)
from app.dependencies.database import SessionDep
from app.infrastructure.repositories.transaction_category_repository import (
    TransactionCategoryRepositoryImpl,
)


def get_transaction_categories_repository(
    session: SessionDep,
) -> TransactionCategoryRepository:
    return TransactionCategoryRepositoryImpl(session)


TransactionCategoryRepositoryDep = Annotated[
    TransactionCategoryRepository,
    Depends(get_transaction_categories_repository),
]
