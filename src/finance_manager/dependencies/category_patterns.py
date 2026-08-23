from typing import Annotated

from fastapi import Depends

from finance_manager.dependencies import SessionDep
from finance_manager.repositories import CategoryPatternRepository


def get_category_pattern_repository(
    session: SessionDep,
) -> CategoryPatternRepository:
    return CategoryPatternRepository(session)


CategoryPatternRepositoryDep = Annotated[
    CategoryPatternRepository,
    Depends(get_category_pattern_repository),
]
