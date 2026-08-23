from typing import Annotated

from fastapi import Depends

from finance_manager.dependencies import SessionDep
from finance_manager.repositories import PersonRepository


def get_person_repository(
    session: SessionDep,
) -> PersonRepository:
    return PersonRepository(session)


PersonRepositoryDep = Annotated[
    PersonRepository,
    Depends(get_person_repository),
]
