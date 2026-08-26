from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.transaction_category import TransactionCategoryRow
from finance_manager.infrastructure.repositories.base import BaseRepository
from finance_manager.schemas.transaction_category import (
    TransactionCategory,
    WriteTransactionCategory,
)


class TransactionCategoryRepository(
    BaseRepository[TransactionCategoryRow, TransactionCategory, WriteTransactionCategory]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionCategoryRow, TransactionCategory, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(
            TransactionCategoryRow.id,
            TransactionCategoryRow.name,
            TransactionCategoryRow.description,
        )

    def _map_create(self, request: WriteTransactionCategory) -> TransactionCategoryRow:
        return TransactionCategoryRow(name=request.name, description=request.description)

    def _map_update(self, request: WriteTransactionCategory, model: TransactionCategoryRow) -> None:
        model.name = request.name
        model.description = request.description


def get_transaction_category_repository(
    session: AsyncSession,
) -> TransactionCategoryRepository:
    return TransactionCategoryRepository(session)
