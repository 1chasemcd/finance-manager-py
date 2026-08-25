from pydantic import Field

from finance_manager.schemas import ApiBase


class WritePerson(ApiBase):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)


class PersonResponse(ApiBase):
    id: int
    first_name: str
    last_name: str
