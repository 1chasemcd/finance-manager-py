from pydantic import Field

from finance_manager.schemas import ApiBase


class WriteCategoryPattern(ApiBase):
    pattern: str = Field(max_length=100)
    transaction_category_id: int | None = Field(default=None, ge=0)


class CategoryPatternResponse(ApiBase):
    id: int
    pattern: str
    transaction_category_id: int | None
    transaction_category_name: str | None
