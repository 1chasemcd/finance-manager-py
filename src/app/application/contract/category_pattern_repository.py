from typing import Protocol

from app.application.contract.repository_capabilities import (
    CreateHandler,
    DeleteHandler,
    LookupHandler,
    SearchHandler,
    UpdateHandler,
)
from app.schemas.category_pattern import CategoryPattern, WriteCategoryPattern


class CategoryPatternRepository(
    LookupHandler[CategoryPattern],
    SearchHandler[CategoryPattern],
    CreateHandler[WriteCategoryPattern],
    UpdateHandler[WriteCategoryPattern],
    DeleteHandler,
    Protocol,
):
    pass
