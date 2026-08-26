from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from finance_manager.infrastructure.autocomplete_registry import autocomplete
from finance_manager.infrastructure.models.db_base import DbBase


@autocomplete("{first_name} {last_name}")
class PersonRow(DbBase):
    __tablename__ = "people"
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
