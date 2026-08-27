from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.transaction_category_row import TransactionCategoryRow
from app.infrastructure.models.transaction_row import TransactionRow
from app.infrastructure.models.transaction_source_row import TransactionSourceRow
from app.infrastructure.repositories.base_repository import BaseRepository
from app.schemas.transaction import (
    SearchTransactions,
    Transaction,
    WriteTransaction,
)


class TransactionRepositoryImpl(
    BaseRepository[
        TransactionRow, Transaction, WriteTransaction, WriteTransaction, SearchTransactions
    ]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionRow, Transaction, session)

    def _select(self) -> Select[tuple[Any, ...]]:
        return (
            select(
                TransactionRow.id,
                TransactionRow.date,
                TransactionRow.amount,
                TransactionRow.summary,
                TransactionRow.transaction_source_id,
                TransactionSourceRow.name.label("transaction_source_name"),
                TransactionRow.transaction_category_id,
                TransactionCategoryRow.name.label("transaction_category_name"),
            )
            .join(TransactionRow.transaction_category)
            .join(TransactionRow.transaction_source)
        )

    def _filter_search(
        self, statement: Select[tuple[Any, ...]], request: SearchTransactions
    ) -> Select[tuple[Any, ...]]:
        statement = super()._filter_search(statement, request)
        if request.min_amount is not None:
            statement = statement.where(TransactionRow.amount >= request.min_amount)
        if request.max_amount is not None:
            statement = statement.where(TransactionRow.amount <= request.max_amount)
        if request.min_date is not None:
            statement = statement.where(TransactionRow.date >= request.min_date)
        if request.max_date is not None:
            statement = statement.where(TransactionRow.date <= request.max_date)
        if request.transaction_source_id is not None:
            statement = statement.where(
                TransactionRow.transaction_source_id == request.transaction_source_id
            )
        if request.transaction_category_id is not None:
            statement = statement.where(
                TransactionRow.transaction_category_id == request.transaction_category_id
            )
        if request.owner_id is not None:
            statement = statement.where(TransactionSourceRow.owner_id == request.owner_id)
        return statement
