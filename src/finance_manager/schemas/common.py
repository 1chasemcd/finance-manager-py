from pydantic import BaseModel, Field


class PagedRequest(BaseModel):
    skip: int = Field(default=0, ge=0)
    take: int = Field(default=50, ge=0, le=50)
