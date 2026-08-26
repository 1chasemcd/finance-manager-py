from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.person_row import PersonRow
from finance_manager.infrastructure.models.transaction_source_row import TransactionSourceRow
from finance_manager.infrastructure.repositories.base_repository import BaseRepository
from finance_manager.schemas.transaction_source import (
    TransactionSource,
    WriteTransactionSource,
)


class TransactionSourceRepositoryImpl(
    BaseRepository[TransactionSourceRow, TransactionSource, WriteTransactionSource]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionSourceRow, TransactionSource, session)

    def _select(self) -> Select[tuple[Any, ...]]:
        return select(
            TransactionSourceRow.id,
            TransactionSourceRow.name,
            TransactionSourceRow.owner_id,
            (PersonRow.first_name + " " + PersonRow.last_name).label("owner_name"),
        ).join(TransactionSourceRow.owner)


def get_transaction_source_repository(
    session: AsyncSession,
) -> TransactionSourceRepository:
    return TransactionSourceRepository(session)
