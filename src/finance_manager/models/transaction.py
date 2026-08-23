from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from finance_manager.models.base import Base

if TYPE_CHECKING:
    from .transaction_category import TransactionCategory
    from .transaction_source import TransactionSource


class Transaction(Base):
    __tablename__ = "transactions"
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    summary: Mapped[str] = mapped_column(String(500))
    transaction_category_id: Mapped[int] = mapped_column(ForeignKey("transaction_categories.id"))
    transaction_category: Mapped[TransactionCategory] = relationship()
    transaction_source_id: Mapped[int] = mapped_column(ForeignKey("transaction_sources.id"))
    transaction_source: Mapped[TransactionSource] = relationship()
