from datetime import datetime
from decimal import Decimal

from pydantic import Field

from finance_manager.schemas import ApiBase


class WriteTransaction(ApiBase):
    timestamp: datetime = Field()
    amount: Decimal = Field(max_digits=12, decimal_places=2)
    summary: str = Field(max_length=500)
    transaction_category_id: int = Field()
    transaction_source_id: int = Field()


class TransactionResponse(ApiBase):
    id: int = Field()
    timestamp: datetime = Field()
    amount: Decimal = Field()
    summary: str = Field()
    transaction_category_id: int = Field()
    transaction_category_name: str = Field()
    transaction_source_id: int = Field()
    transaction_source_name: str = Field()
