from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.autocomplete_registry import autocomplete
from app.infrastructure.models.db_base import DbBase


@autocomplete("{name}")
class TransactionCategoryRow(DbBase):
    __tablename__ = "transaction_categories"
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str | None] = mapped_column(String(500))
