from pydantic import BaseModel, Field


class WriteCategoryPattern(BaseModel):
    pattern: str = Field(max_length=100)
    transaction_category_id: int = Field(ge=0)


class CategoryPatternResponse(BaseModel):
    id: int = Field()
    pattern: str = Field(max_length=100)
    transaction_category_id: int = Field()
    transaction_category_name: str = Field()
