from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.person_row import PersonRow
from app.infrastructure.models.transaction_source_row import TransactionSourceRow
from app.infrastructure.repositories.base_repository import BaseRepository
from app.schemas.transaction_source import (
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
            TransactionSourceRow.import_def_id,
            (PersonRow.first_name + " " + PersonRow.last_name).label("owner_name"),
        ).join(TransactionSourceRow.owner)
