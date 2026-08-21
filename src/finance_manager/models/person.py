from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from finance_manager.models.base import Base


class Person(Base):
    __tablename__ = "people"
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
