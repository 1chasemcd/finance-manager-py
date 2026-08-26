from typing import Annotated

from fastapi import Depends

from app.application.contract.autocomplete_repository import AutocompleteRepository
from app.dependencies.database import SessionDep
from app.infrastructure.autocomplete_registry import AutocompleteRegistry
from app.infrastructure.repositories.autocomplete_repository import (
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
