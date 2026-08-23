from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from finance_manager.core import autocomplete
from finance_manager.models.base import Base


@autocomplete("{name}")
class TransactionCategory(Base):
    __tablename__ = "transaction_categories"
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(500))
