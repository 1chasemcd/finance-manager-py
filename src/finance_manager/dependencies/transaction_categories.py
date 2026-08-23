from typing import Annotated

from fastapi import Depends

from finance_manager.dependencies import SessionDep
from finance_manager.repositories import TransactionCategoryRepository


def get_transaction_categories_repository(
    session: SessionDep,
) -> TransactionCategoryRepository:
    return TransactionCategoryRepository(session)


TransactionCategoryRepositoryDep = Annotated[
    TransactionCategoryRepository,
    Depends(get_transaction_categories_repository),
]
