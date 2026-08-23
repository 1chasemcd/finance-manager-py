from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.models.person import Person
from finance_manager.repositories.base import BaseRepository
from finance_manager.schemas.person import PersonResponse, WritePerson


class PersonRepository(BaseRepository[Person, PersonResponse, WritePerson]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(Person, PersonResponse, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(Person.first_name, Person.last_name)

    def _map_create(self, request: WritePerson) -> Person:
        return Person(first_name=request.first_name, last_name=request.last_name)

    def _map_update(self, request: WritePerson, model: Person) -> None:
        model.first_name = request.first_name
        model.last_name = request.last_name


def get_person_repository(
    session: AsyncSession,
) -> PersonRepository:
    return PersonRepository(session)
