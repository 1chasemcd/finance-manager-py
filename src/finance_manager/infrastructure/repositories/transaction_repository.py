from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.transaction import TransactionRow
from finance_manager.infrastructure.models.transaction_category import TransactionCategoryRow
from finance_manager.infrastructure.models.transaction_source import TransactionSourceRow
from finance_manager.infrastructure.repositories.base import BaseRepository
from finance_manager.schemas.transaction import (
    Transaction,
    TransactionsQuery,
    WriteTransaction,
)


class TransactionRepository(
    BaseRepository[
        TransactionRow, Transaction, WriteTransaction, WriteTransaction, TransactionsQuery
    ]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionRow, Transaction, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return (
            select(
                TransactionRow.id,
                TransactionRow.timestamp,
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

    def _map_create(self, request: WriteTransaction) -> TransactionRow:
        return TransactionRow(
            timestamp=request.timestamp,
            amount=request.amount,
            summary=request.summary,
            transaction_source_id=request.transaction_source_id,
            transaction_category_id=request.transaction_category_id,
        )

    def _map_update(self, request: WriteTransaction, model: TransactionRow) -> None:
        model.timestamp = request.timestamp
        model.amount = request.amount
        model.summary = request.summary
        model.transaction_source_id = request.transaction_source_id
        model.transaction_category_id = request.transaction_category_id

    def _filter_search(
        self, statement: Select[tuple[Any, ...]], request: TransactionsQuery
    ) -> Select[tuple[Any, ...]]:
        statement = super()._filter_search(statement, request)
        if request.min_amount is not None:
            statement = statement.where(TransactionRow.amount >= request.min_amount)
        if request.max_amount is not None:
            statement = statement.where(TransactionRow.amount <= request.max_amount)
        if request.min_date is not None:
            statement = statement.where(TransactionRow.timestamp >= request.min_date)
        if request.max_date is not None:
            statement = statement.where(TransactionRow.timestamp <= request.max_date)
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


def get_transaction_repository(
    session: AsyncSession,
) -> TransactionRepository:
    return TransactionRepository(session)
