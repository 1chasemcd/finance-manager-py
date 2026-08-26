from typing import Protocol

from pydantic import BaseModel, ConfigDict, Field

from app.core.string_utils import snake_to_camel


class SchemaBase(BaseModel):
    model_config = ConfigDict(
        alias_generator=snake_to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )


class HasPage(Protocol):
    skip: int
    take: int


class PagedQuery(SchemaBase):
    skip: int = Field(default=0, ge=0)
    take: int = Field(default=50, ge=0, le=50)


class AutocompleteRequest(PagedQuery):
    search: str = Field(max_length=500)


class SearchResponse[TModel](SchemaBase):
    total: int
    result: list[TModel]
