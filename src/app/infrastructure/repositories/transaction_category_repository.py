from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.transaction_category_row import TransactionCategoryRow
from app.infrastructure.repositories.base_repository import BaseRepository
from app.schemas.transaction_category import (
    TransactionCategory,
    WriteTransactionCategory,
)


class TransactionCategoryRepositoryImpl(
    BaseRepository[TransactionCategoryRow, TransactionCategory, WriteTransactionCategory]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionCategoryRow, TransactionCategory, session)
