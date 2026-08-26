from datetime import datetime
from decimal import Decimal

from pydantic import Field

from finance_manager.schemas import SchemaBase
from finance_manager.schemas.common import PagedQuery


class TransactionsQuery(PagedQuery):
    min_date: datetime | None = None
    max_date: datetime | None = None
    min_amount: Decimal | None = None
    max_amount: Decimal | None = None
    transaction_category_id: int | None = None
    transaction_source_id: int | None = None
    owner_id: int | None = None


class WriteTransaction(SchemaBase):
    timestamp: datetime
    amount: Decimal = Field(max_digits=12, decimal_places=2)
    summary: str = Field(max_length=500)
    transaction_category_id: int
    transaction_source_id: int


class Transaction(SchemaBase):
    id: int
    timestamp: datetime
    amount: Decimal
    summary: str
    transaction_category_id: int
    transaction_category_name: str
    transaction_source_id: int
    transaction_source_name: str
