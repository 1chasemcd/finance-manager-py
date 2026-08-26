from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.infrastructure.models.category_pattern import CategoryPatternRow
from finance_manager.infrastructure.models.transaction_category import TransactionCategoryRow
from finance_manager.infrastructure.repositories.base import BaseRepository
from finance_manager.schemas.category_pattern import (
    CategoryPattern,
    WriteCategoryPattern,
)


class CategoryPatternRepository(
    BaseRepository[CategoryPatternRow, CategoryPattern, WriteCategoryPattern]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(CategoryPatternRow, CategoryPattern, session)

    def _select_statement(self) -> Select[tuple[Any, ...]]:
        return select(
            CategoryPatternRow.id,
            CategoryPatternRow.pattern,
            CategoryPatternRow.transaction_category_id,
            TransactionCategoryRow.name.label("transaction_category_name"),
        ).outerjoin(CategoryPatternRow.transaction_category)

    def _map_create(self, request: WriteCategoryPattern) -> CategoryPatternRow:
        return CategoryPatternRow(
            pattern=request.pattern, transaction_category_id=request.transaction_category_id
        )

    def _map_update(self, request: WriteCategoryPattern, model: CategoryPatternRow) -> None:
        model.pattern = request.pattern
        model.transaction_category_id = request.transaction_category_id


def get_category_pattern_repository(
    session: AsyncSession,
) -> CategoryPatternRepository:
    return CategoryPatternRepository(session)
