from typing import Protocol

from app.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from app.schemas.person import Person, WritePerson


class PersonRepository(
    LookupHandler[Person],
    SearchHandler[Person],
    CreateHandler[WritePerson],
    UpdateHandler[WritePerson],
    DeleteHandler,
    Protocol,
):
    pass
