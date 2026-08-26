from pydantic import Field

from app.schemas.common import SchemaBase


class WriteTransactionSource(SchemaBase):
    name: str = Field(max_length=100)
    owner_id: int = Field(ge=0)


class TransactionSource(SchemaBase):
    id: int
    name: str
    owner_id: int
    owner_name: str
