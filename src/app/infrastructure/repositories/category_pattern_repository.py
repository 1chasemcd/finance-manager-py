from typing import Any

from sqlalchemy import Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.models.category_pattern_row import CategoryPatternRow
from app.infrastructure.models.transaction_category_row import TransactionCategoryRow
from app.infrastructure.repositories.base_repository import BaseRepository
from app.schemas.category_pattern import (
    CategoryPattern,
    WriteCategoryPattern,
)


class CategoryPatternRepositoryImpl(
    BaseRepository[CategoryPatternRow, CategoryPattern, WriteCategoryPattern]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(CategoryPatternRow, CategoryPattern, session)

    def _select(self) -> Select[tuple[Any, ...]]:
        return select(
            CategoryPatternRow.id,
            CategoryPatternRow.pattern,
            CategoryPatternRow.transaction_category_id,
            TransactionCategoryRow.name.label("transaction_category_name"),
        ).outerjoin(CategoryPatternRow.transaction_category)
