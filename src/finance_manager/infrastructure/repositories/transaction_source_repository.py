from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.person import PersonRow
from finance_manager.infrastructure.models.transaction_source import TransactionSourceRow
from finance_manager.infrastructure.repositories.base import BaseRepository
from finance_manager.schemas.transaction_source import (
    TransactionSource,
    WriteTransactionSource,
)


class TransactionSourceRepository(
    BaseRepository[TransactionSourceRow, TransactionSource, WriteTransactionSource]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionSourceRow, TransactionSource, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(
            TransactionSourceRow.id,
            TransactionSourceRow.name,
            TransactionSourceRow.owner_id,
            (PersonRow.first_name + " " + PersonRow.last_name).label("owner_name"),
        ).join(TransactionSourceRow.owner)

    def _map_create(self, request: WriteTransactionSource) -> TransactionSourceRow:
        return TransactionSourceRow(name=request.name, owner_id=request.owner_id)

    def _map_update(self, request: WriteTransactionSource, model: TransactionSourceRow) -> None:
        model.name = request.name
        model.owner_id = request.owner_id


def get_transaction_source_repository(
    session: AsyncSession,
) -> TransactionSourceRepository:
    return TransactionSourceRepository(session)
