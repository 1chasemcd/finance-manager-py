from pydantic import BaseModel, Field


class WritePerson(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)


class PersonResponse(BaseModel):
    id: int = Field()
    first_name: str = Field()
    last_name: str = Field()
