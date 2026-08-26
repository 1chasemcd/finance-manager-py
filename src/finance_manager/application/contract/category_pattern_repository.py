from typing import Protocol

from finance_manager.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from finance_manager.schemas.category_pattern import CategoryPattern, WriteCategoryPattern


class CategoryPatternRepository(
    LookupHandler[CategoryPattern],
    SearchHandler[CategoryPattern],
    CreateHandler[WriteCategoryPattern],
    UpdateHandler[WriteCategoryPattern],
    DeleteHandler,
    Protocol,
):
    pass
