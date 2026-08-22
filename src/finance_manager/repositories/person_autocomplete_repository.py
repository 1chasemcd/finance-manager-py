from sqlalchemy import Select, select

from finance_manager.models import Person
from finance_manager.repositories import AutocompleteRepository


class PersonAutocompleteRepository(AutocompleteRepository):
    def _statement(self) -> Select[tuple[int, str]]:
        return select(Person.id, Person.first_name + " " + Person.last_name)
