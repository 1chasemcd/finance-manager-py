from pydantic import Field

from finance_manager.schemas import ApiBase


class WriteTransactionSource(ApiBase):
    name: str = Field(max_length=100)
    owner_id: int = Field(ge=0)


class TransactionSourceResponse(ApiBase):
    id: int = Field()
    name: str = Field()
    owner_id: int = Field()
    owner_name: str = Field()
