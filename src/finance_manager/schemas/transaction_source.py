from pydantic import BaseModel, Field


class WriteTransactionSource(BaseModel):
    name: str = Field(max_length=100)
    owner_id: int = Field(ge=0)


class TransactionSourceResponse(BaseModel):
    id: int = Field()
    name: str = Field(max_length=100)
    owner_id: int = Field()
    owner_name: str = Field()
