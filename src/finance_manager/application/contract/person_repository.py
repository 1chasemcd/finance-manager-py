from typing import Protocol

from finance_manager.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from finance_manager.schemas.person import Person, WritePerson


class PersonRepository(
    LookupHandler[Person],
    SearchHandler[Person],
    CreateHandler[WritePerson],
    UpdateHandler[WritePerson],
    DeleteHandler,
    Protocol,
):
    pass
