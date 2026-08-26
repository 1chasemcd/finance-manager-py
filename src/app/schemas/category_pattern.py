from pydantic import Field

from app.schemas.common import SchemaBase


class WriteCategoryPattern(SchemaBase):
    pattern: str = Field(max_length=100)
    transaction_category_id: int | None = Field(default=None, ge=0)


class CategoryPattern(SchemaBase):
    id: int
    pattern: str
    transaction_category_id: int | None
    transaction_category_name: str | None
