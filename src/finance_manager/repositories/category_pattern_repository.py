from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.models.category_pattern import CategoryPattern
from finance_manager.models.transaction_category import TransactionCategory
from finance_manager.repositories.base import BaseRepository
from finance_manager.schemas.category_pattern import (
    CategoryPatternResponse,
    WriteCategoryPattern,
)


class CategoryPatternRepository(
    BaseRepository[CategoryPattern, CategoryPatternResponse, WriteCategoryPattern]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(CategoryPattern, CategoryPatternResponse, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(
            CategoryPattern.id,
            CategoryPattern.pattern,
            CategoryPattern.transaction_category_id,
            TransactionCategory.name.label("transaction_category_name"),
        ).outerjoin(CategoryPattern.transaction_category)

    def _map_create(self, request: WriteCategoryPattern) -> CategoryPattern:
        return CategoryPattern(
            pattern=request.pattern, transaction_category_id=request.transaction_category_id
        )

    def _map_update(self, request: WriteCategoryPattern, model: CategoryPattern) -> None:
        model.pattern = request.pattern
        model.transaction_category_id = request.transaction_category_id


def get_category_pattern_repository(
    session: AsyncSession,
) -> CategoryPatternRepository:
    return CategoryPatternRepository(session)
