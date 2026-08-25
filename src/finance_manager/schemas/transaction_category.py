from pydantic import Field

from finance_manager.schemas import ApiBase


class WriteTransactionCategory(ApiBase):
    name: str = Field(max_length=100)
    description: str | None = Field(default=None, max_length=500)


class TransactionCategoryResponse(ApiBase):
    id: int
    name: str
    description: str | None
