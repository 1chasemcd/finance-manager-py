from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from finance_manager.core.autocomplete_registry import autocomplete
from finance_manager.models.base import DbBase


@autocomplete("{name}")
class TransactionCategory(DbBase):
    __tablename__ = "transaction_categories"
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None] = mapped_column(String(500))
