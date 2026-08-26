from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.person_row import PersonRow
from app.infrastructure.repositories.base_repository import BaseRepository
from app.schemas.person import Person, WritePerson


class PersonRepositoryImpl(BaseRepository[PersonRow, Person, WritePerson]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(PersonRow, Person, session)
