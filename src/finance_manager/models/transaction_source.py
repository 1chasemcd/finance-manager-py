from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from finance_manager.core.autocomplete_registry import autocomplete
from finance_manager.models.base import DbBase

if TYPE_CHECKING:
    from .person import Person


@autocomplete("{name}")
class TransactionSource(DbBase):
    __tablename__ = "transaction_sources"
    name: Mapped[str] = mapped_column(String(100), unique=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("people.id"))
    owner: Mapped[Person] = relationship()
