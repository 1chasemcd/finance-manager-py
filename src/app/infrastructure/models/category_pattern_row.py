from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.models.db_base import DbBase

if TYPE_CHECKING:
    from .transaction_category_row import TransactionCategoryRow


class CategoryPatternRow(DbBase):
    __tablename__ = "category_patterns"
    pattern: Mapped[str] = mapped_column(String(100), unique=True)
    transaction_category_id: Mapped[int | None] = mapped_column(
        ForeignKey("transaction_categories.id")
    )
    transaction_category: Mapped[TransactionCategoryRow | None] = relationship()
