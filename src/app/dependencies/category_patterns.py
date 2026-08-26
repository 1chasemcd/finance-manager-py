from typing import Annotated

from fastapi import Depends

from app.application.contract.category_pattern_repository import (
    CategoryPatternRepository,
)
from app.dependencies.database import SessionDep
from app.infrastructure.repositories.category_pattern_repository import (
    CategoryPatternRepositoryImpl,
)


def get_category_pattern_repository(
    session: SessionDep,
) -> CategoryPatternRepository:
    return CategoryPatternRepositoryImpl(session)


CategoryPatternRepositoryDep = Annotated[
    CategoryPatternRepository,
    Depends(get_category_pattern_repository),
]
