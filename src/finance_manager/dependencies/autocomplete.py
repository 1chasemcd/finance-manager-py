from typing import Annotated

from fastapi import Depends

from finance_manager.application.contract.autocomplete_repository import AutocompleteRepository
from finance_manager.dependencies import SessionDep
from finance_manager.infrastructure.autocomplete_registry import AutocompleteRegistry
from finance_manager.infrastructure.repositories.autocomplete_repository import (
    AutocompleteRepositoryImpl,
)


def get_autocomplete_registry() -> AutocompleteRegistry:
    return AutocompleteRegistry()


AutocompleteRegistryDep = Annotated[
    AutocompleteRegistry,
    Depends(get_autocomplete_registry),
]


def get_autocomplete_repository(
    session: SessionDep,
    registry: AutocompleteRegistryDep,
) -> AutocompleteRepository:
    return AutocompleteRepositoryImpl(session, registry)


AutocompleteRepositoryDep = Annotated[
    AutocompleteRepository,
    Depends(get_autocomplete_repository),
]
