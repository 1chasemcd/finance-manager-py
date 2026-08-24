from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.models.person import Person
from finance_manager.models.transaction_source import TransactionSource
from finance_manager.repositories.base import BaseRepository
from finance_manager.schemas.transaction_source import (
    TransactionSourceResponse,
    WriteTransactionSource,
)


class TransactionSourceRepository(
    BaseRepository[TransactionSource, TransactionSourceResponse, WriteTransactionSource]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(TransactionSource, TransactionSourceResponse, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(
            TransactionSource.id,
            TransactionSource.name,
            TransactionSource.owner_id,
            (Person.first_name + " " + Person.last_name).label("owner_name"),
        ).join(TransactionSource.owner)

    def _map_create(self, request: WriteTransactionSource) -> TransactionSource:
        return TransactionSource(name=request.name, owner_id=request.owner_id)

    def _map_update(self, request: WriteTransactionSource, model: TransactionSource) -> None:
        model.name = request.name
        model.owner_id = request.owner_id


def get_transaction_source_repository(
    session: AsyncSession,
) -> TransactionSourceRepository:
    return TransactionSourceRepository(session)
