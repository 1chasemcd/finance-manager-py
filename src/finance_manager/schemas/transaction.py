from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class WriteTransaction(BaseModel):
    timestamp: datetime = Field()
    amount: Decimal = Field(max_digits=12, decimal_places=2)
    summary: str = Field(max_length=500)
    transaction_category_id: int = Field()
    transaction_source_id: int = Field()


class TransactionResponse(BaseModel):
    timestamp: datetime = Field()
    amount: Decimal = Field(max_digits=12, decimal_places=2)
    summary: str = Field(max_length=500)
    transaction_category_id: int = Field()
    transaction_category_name: str = Field()
    transaction_source_name: str = Field()
