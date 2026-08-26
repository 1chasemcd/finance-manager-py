from pydantic import Field

from app.schemas.common import SchemaBase


class WriteTransactionCategory(SchemaBase):
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=500)


class TransactionCategory(SchemaBase):
    id: int
    name: str
    description: str | None
