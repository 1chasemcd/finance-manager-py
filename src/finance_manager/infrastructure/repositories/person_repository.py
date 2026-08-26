from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.person import PersonRow
from finance_manager.infrastructure.repositories.base import BaseRepository
from finance_manager.schemas.person import Person, WritePerson


class PersonRepository(BaseRepository[PersonRow, Person, WritePerson]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(PersonRow, Person, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(PersonRow.id, PersonRow.first_name, PersonRow.last_name)

    def _map_create(self, request: WritePerson) -> PersonRow:
        return PersonRow(first_name=request.first_name, last_name=request.last_name)

    def _map_update(self, request: WritePerson, model: PersonRow) -> None:
        model.first_name = request.first_name
        model.last_name = request.last_name


def get_person_repository(
    session: AsyncSession,
) -> PersonRepository:
    return PersonRepository(session)
