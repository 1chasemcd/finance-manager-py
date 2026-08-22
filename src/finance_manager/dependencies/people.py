from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.dependencies.database import get_db_session
from finance_manager.repositories import PersonAutocompleteRepository, PersonRepository

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]


def get_person_repository(
    session: SessionDep,
) -> PersonRepository:
    return PersonRepository(session)


PersonRepositoryDep = Annotated[
    PersonRepository,
    Depends(get_person_repository),
]


def get_person_autocomplete_repository(
    session: SessionDep,
) -> PersonAutocompleteRepository:
    return PersonAutocompleteRepository(session)


PersonAutocompleteRepositoryDep = Annotated[
    PersonAutocompleteRepository,
    Depends(get_person_autocomplete_repository),
]
