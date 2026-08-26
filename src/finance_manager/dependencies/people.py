from typing import Annotated

from fastapi import Depends

from finance_manager.application.contract.person_repository import PersonRepository
from finance_manager.dependencies.database import SessionDep
from finance_manager.infrastructure.repositories.person_repository import PersonRepositoryImpl


def get_person_repository(
    session: SessionDep,
) -> PersonRepository:
    return PersonRepositoryImpl(session)


PersonRepositoryDep = Annotated[
    PersonRepository,
    Depends(get_person_repository),
]
