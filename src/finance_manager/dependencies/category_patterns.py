from typing import Annotated

from fastapi import Depends

from finance_manager.application.contract.category_pattern_repository import (
    CategoryPatternRepository,
)
from finance_manager.dependencies.database import SessionDep
from finance_manager.infrastructure.repositories.category_pattern_repository import (
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
