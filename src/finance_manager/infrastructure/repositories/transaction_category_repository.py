from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.transaction_category_row import TransactionCategoryRow
from finance_manager.infrastructure.repositories.base_repository import BaseRepository
from finance_manager.schemas.transaction_category import (
    TransactionCategory,
    WriteTransactionCategory,
)


class TransactionCategoryRepositoryImpl(
    BaseRepository[TransactionCategoryRow, TransactionCategory, WriteTransactionCategory]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionCategoryRow, TransactionCategory, session)


def get_transaction_category_repository(
    session: AsyncSession,
) -> TransactionCategoryRepository:
    return TransactionCategoryRepositoryImpl(session)
