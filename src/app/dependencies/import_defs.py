from typing import Annotated

from fastapi import Depends

from app.application.contract.import_def_repository import (
    ImportDefRepository,
)
from app.dependencies.database import SessionDep
from app.infrastructure.repositories.import_def_repository import (
    ImportDefRepositoryImpl,
)


def get_import_def_repository(
    session: SessionDep,
) -> ImportDefRepository:
    return ImportDefRepositoryImpl(session)


ImportDefRepositoryDep = Annotated[
    ImportDefRepository,
    Depends(get_import_def_repository),
]
