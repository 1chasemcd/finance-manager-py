from sqlalchemy import Boolean, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.autocomplete_registry import autocomplete
from app.infrastructure.models.db_base import DbBase


@autocomplete("importdef", "{name}")
class ImportDefRow(DbBase):
    __tablename__ = "import_defs"
    name: Mapped[str] = mapped_column(String(100), unique=True)

    skip_rows: Mapped[int] = mapped_column(SmallInteger)
    row_pattern: Mapped[str | None] = mapped_column(String(500))

    date_index: Mapped[int] = mapped_column(SmallInteger)
    summary_index: Mapped[int] = mapped_column(SmallInteger)
    amount_index: Mapped[int] = mapped_column(SmallInteger)

    date_format: Mapped[str] = mapped_column(String(100))
    positive_is_spending: Mapped[bool] = mapped_column(Boolean)
