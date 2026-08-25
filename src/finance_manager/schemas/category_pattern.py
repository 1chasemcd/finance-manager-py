from pydantic import Field

from finance_manager.schemas import ApiBase


class WriteCategoryPattern(ApiBase):
    pattern: str = Field(max_length=100)
    transaction_category_id: int = Field(ge=0)


class CategoryPatternResponse(ApiBase):
    id: int = Field()
    pattern: str = Field()
    transaction_category_id: int | None = Field()
    transaction_category_name: str | None = Field()
