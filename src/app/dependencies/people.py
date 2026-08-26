from typing import Annotated

from fastapi import Depends

from app.application.contract.person_repository import PersonRepository
from app.dependencies.database import SessionDep
from app.infrastructure.repositories.person_repository import PersonRepositoryImpl


def get_person_repository(
    session: SessionDep,
) -> PersonRepository:
    return PersonRepositoryImpl(session)


PersonRepositoryDep = Annotated[
    PersonRepository,
    Depends(get_person_repository),
]
