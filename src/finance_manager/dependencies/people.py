from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.dependencies.database import get_db_session
from finance_manager.repositories import PersonRepository
from finance_manager.schemas.person import PersonResponse, WritePerson
from finance_manager.services import EntityCommandService, EntityQueryService

PersonQueryService = EntityQueryService[PersonResponse]
PersonCommandService = EntityCommandService[WritePerson]

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]


def get_person_repository(
    session: SessionDep,
) -> PersonRepository:
    return PersonRepository(session)


PersonRepositoryDep = Annotated[
    PersonRepository,
    Depends(get_person_repository),
]


def get_person_query_service(repository: PersonRepositoryDep) -> PersonQueryService:
    return PersonQueryService(repository)


PersonQueryServiceDep = Annotated[
    PersonQueryService,
    Depends(get_person_query_service),
]


def get_person_command_service(repository: PersonRepositoryDep) -> PersonCommandService:
    return PersonCommandService(repository)


PersonCommandServiceDep = Annotated[
    PersonCommandService,
    Depends(get_person_command_service),
]
