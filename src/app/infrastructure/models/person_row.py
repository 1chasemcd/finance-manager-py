from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.autocomplete_registry import autocomplete
from app.infrastructure.models.db_base import DbBase


@autocomplete("person", "{first_name} {last_name}")
class PersonRow(DbBase):
    __tablename__ = "people"
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
