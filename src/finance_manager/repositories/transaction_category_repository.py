from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.models.transaction_category import TransactionCategory
from finance_manager.repositories.base import BaseRepository
from finance_manager.schemas.transaction_category import (
    TransactionCategoryResponse,
    WriteTransactionCategory,
)


class TransactionCategoryRepository(
    BaseRepository[TransactionCategory, TransactionCategoryResponse, WriteTransactionCategory]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionCategory, TransactionCategoryResponse, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(
            TransactionCategory.id, TransactionCategory.name, TransactionCategory.description
        )

    def _map_create(self, request: WriteTransactionCategory) -> TransactionCategory:
        return TransactionCategory(name=request.name, description=request.description)

    def _map_update(self, request: WriteTransactionCategory, model: TransactionCategory) -> None:
        model.name = request.name
        model.description = request.description


def get_transaction_category_repository(
    session: AsyncSession,
) -> TransactionCategoryRepository:
    return TransactionCategoryRepository(session)
