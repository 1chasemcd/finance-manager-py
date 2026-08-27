from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.models.db_base import DbBase

if TYPE_CHECKING:
    from .transaction_category_row import TransactionCategoryRow
    from .transaction_source_row import TransactionSourceRow


class TransactionRow(DbBase):
    __tablename__ = "transactions"
    date: Mapped[datetime] = mapped_column(DateTime)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    summary: Mapped[str] = mapped_column(String(500))
    transaction_category_id: Mapped[int] = mapped_column(ForeignKey("transaction_categories.id"))
    transaction_category: Mapped[TransactionCategoryRow] = relationship()
    transaction_source_id: Mapped[int] = mapped_column(ForeignKey("transaction_sources.id"))
    transaction_source: Mapped[TransactionSourceRow] = relationship()
