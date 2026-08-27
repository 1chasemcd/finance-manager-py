from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.autocomplete_registry import autocomplete
from app.infrastructure.models.db_base import DbBase
from app.infrastructure.models.import_def_row import ImportDefRow

if TYPE_CHECKING:
    from .person_row import PersonRow


@autocomplete("transactionsource", "{name}")
class TransactionSourceRow(DbBase):
    __tablename__ = "transaction_sources"
    name: Mapped[str] = mapped_column(String(100), unique=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("people.id"))
    owner: Mapped[PersonRow] = relationship()
    import_def_id: Mapped[int] = mapped_column(ForeignKey("import_defs.id"))
    import_def: Mapped[ImportDefRow] = relationship()
