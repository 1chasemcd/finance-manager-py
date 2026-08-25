from typing import Protocol

from pydantic import BaseModel, ConfigDict, Field


def to_camel(s: str) -> str:
    parts = s.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


class ApiBase(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_name=True,
        validate_by_alias=True,
    )


class HasPage(Protocol):
    skip: int
    take: int


class PagedRequest(ApiBase):
    skip: int = Field(default=0, ge=0)
    take: int = Field(default=50, ge=0, le=50)


class AutocompleteRequest(ApiBase):
    search: str = Field(max_length=500)
