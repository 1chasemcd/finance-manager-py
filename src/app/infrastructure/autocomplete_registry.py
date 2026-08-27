import re
from collections.abc import Callable
from dataclasses import dataclass

from sqlalchemy import ColumnElement, SQLColumnExpression, literal

from app.infrastructure.models.db_base import DbBase

from ..core.errors import NotFound
from ..core.result import Ok, Result


@dataclass
class _AutocompleteRegistryEntry:
    id: SQLColumnExpression[int]
    display: SQLColumnExpression[str]


_autocomplete_registry: dict[str, _AutocompleteRegistryEntry] = {}


def _build_expression[T: DbBase](cls: type[T], template: str) -> ColumnElement[str]:
    parts = re.split(r"(\{[^}]+\})", template)

    expression: ColumnElement[str] | None = None

    for part in parts:
        if not part:
            continue

        if part.startswith("{") and part.endswith("}"):
            value = getattr(cls, part[1:-1])
        else:
            value = literal(part)

        expression = value if expression is None else expression + value

    assert expression is not None
    return expression


def autocomplete[T: DbBase](
    name: str,
    template: str,
) -> Callable[[type[T]], type[T]]:
    def decorator(cls: type[T]) -> type[T]:
        _autocomplete_registry[name] = _AutocompleteRegistryEntry(
            id=cls.id, display=_build_expression(cls, template)
        )
        return cls

    return decorator


class AutocompleteRegistry:
    def get(self, name: str) -> Result[_AutocompleteRegistryEntry]:
        find = name.lower()
        return Ok(_autocomplete_registry[find]) if find in _autocomplete_registry else NotFound()
