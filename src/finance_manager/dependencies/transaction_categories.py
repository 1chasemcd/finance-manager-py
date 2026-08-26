from typing import Annotated

from fastapi import Depends

from finance_manager.application.contract.transaction_category_repository import (
    TransactionCategoryRepository,
)
from finance_manager.dependencies import SessionDep
from finance_manager.infrastructure.repositories.transaction_category_repository import (
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
