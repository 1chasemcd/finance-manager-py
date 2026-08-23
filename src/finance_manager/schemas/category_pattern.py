from pydantic import BaseModel, Field


class WriteCategoryPattern(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)


class CategoryPatternResponse(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
