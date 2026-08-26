from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from finance_manager.infrastructure.autocomplete_registry import autocomplete
from finance_manager.infrastructure.models.db_base import DbBase

if TYPE_CHECKING:
    from .person_row import PersonRow


@autocomplete("{name}")
class TransactionSourceRow(DbBase):
    __tablename__ = "transaction_sources"
    name: Mapped[str] = mapped_column(String(100), unique=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("people.id"))
    owner: Mapped[PersonRow] = relationship()
