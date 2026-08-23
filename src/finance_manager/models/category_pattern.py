from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from finance_manager.models.base import Base

if TYPE_CHECKING:
    from .transaction_category import TransactionCategory


class CategoryPattern(Base):
    __tablename__ = "category_patterns"
    pattern: Mapped[str] = mapped_column(String(100), unique=True)
    transaction_category_id: Mapped[int | None] = mapped_column(
        ForeignKey("transaction_categories.id")
    )
    transaction_category: Mapped[TransactionCategory | None] = relationship()
