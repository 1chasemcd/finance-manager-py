from pydantic import Field

from app.schemas.common import SchemaBase


class WritePerson(SchemaBase):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)


class Person(SchemaBase):
    id: int
    first_name: str
    last_name: str
