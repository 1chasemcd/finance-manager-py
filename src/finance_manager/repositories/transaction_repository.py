from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.models.transaction import Transaction
from finance_manager.models.transaction_category import TransactionCategory
from finance_manager.models.transaction_source import TransactionSource
from finance_manager.repositories.base import BaseRepository
from finance_manager.schemas.transaction import (
    SearchTransactions,
    TransactionResponse,
    WriteTransaction,
)


class TransactionRepository(
    BaseRepository[
        Transaction, TransactionResponse, WriteTransaction, WriteTransaction, SearchTransactions
    ]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Transaction, TransactionResponse, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return (
            select(
                Transaction.id,
                Transaction.timestamp,
                Transaction.amount,
                Transaction.summary,
                Transaction.transaction_source_id,
                TransactionSource.name.label("transaction_source_name"),
                Transaction.transaction_category_id,
                TransactionCategory.name.label("transaction_category_name"),
            )
            .join(Transaction.transaction_category)
            .join(Transaction.transaction_source)
        )

    def _map_create(self, request: WriteTransaction) -> Transaction:
        return Transaction(
            timestamp=request.timestamp,
            amount=request.amount,
            summary=request.summary,
            transaction_source_id=request.transaction_source_id,
            transaction_category_id=request.transaction_category_id,
        )

    def _map_update(self, request: WriteTransaction, model: Transaction) -> None:
        model.timestamp = request.timestamp
        model.amount = request.amount
        model.summary = request.summary
        model.transaction_source_id = request.transaction_source_id
        model.transaction_category_id = request.transaction_category_id

    def _filter_search(
        self, statement: Select[tuple[Any, ...]], request: SearchTransactions
    ) -> Select[tuple[Any, ...]]:
        statement = super()._filter_search(statement, request)
        if request.min_amount is not None:
            statement = statement.where(Transaction.amount >= request.min_amount)
        if request.max_amount is not None:
            statement = statement.where(Transaction.amount <= request.max_amount)
        if request.min_date is not None:
            statement = statement.where(Transaction.timestamp >= request.min_date)
        if request.max_date is not None:
            statement = statement.where(Transaction.timestamp <= request.max_date)
        if request.transaction_source_id is not None:
            statement = statement.where(
                Transaction.transaction_source_id == request.transaction_source_id
            )
        if request.transaction_category_id is not None:
            statement = statement.where(
                Transaction.transaction_category_id == request.transaction_category_id
            )
        if request.owner_id is not None:
            statement = statement.where(TransactionSource.owner_id == request.owner_id)
        return statement


def get_transaction_repository(
    session: AsyncSession,
) -> TransactionRepository:
    return TransactionRepository(session)
