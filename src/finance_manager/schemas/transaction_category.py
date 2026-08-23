from pydantic import BaseModel, Field


class WriteTransactionCategory(BaseModel):
    name: str = Field(max_length=100)
    description: str | None = Field(max_length=500)


class TransactionCategoryResponse(BaseModel):
    id: int = Field()
    name: str = Field(max_length=100)
    description: str | None = Field(max_length=500)
