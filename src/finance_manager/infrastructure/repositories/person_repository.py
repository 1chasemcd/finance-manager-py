from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.person_row import PersonRow
from finance_manager.infrastructure.repositories.base_repository import BaseRepository
from finance_manager.schemas.person import Person, WritePerson


class PersonRepository(BaseRepository[PersonRow, Person, WritePerson]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(PersonRow, Person, session)


def get_person_repository(
    session: AsyncSession,
) -> PersonRepository:
    return PersonRepository(session)
