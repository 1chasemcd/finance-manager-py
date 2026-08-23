import re
from collections.abc import Callable
from dataclasses import dataclass

from sqlalchemy import ColumnElement, SQLColumnExpression, literal

from finance_manager.models import Base

from .errors import NotFound
from .result import Ok, Result


@dataclass
class _AutocompleteRegistryEntry:
    id: SQLColumnExpression[int]
    display: SQLColumnExpression[str]


_autocomplete_registry: dict[str, _AutocompleteRegistryEntry] = {}


def _build_expression[T: Base](cls: type[T], template: str) -> ColumnElement[str]:
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


def autocomplete[T: Base](
    template: str,
) -> Callable[[type[T]], type[T]]:
    def decorator(cls: type[T]) -> type[T]:
        _autocomplete_registry[cls.__name__.lower()] = _AutocompleteRegistryEntry(
            id=cls.id, display=_build_expression(cls, template)
        )
        return cls

    return decorator


class AutocompleteRegistry:
    def get(self, name: str) -> Result[_AutocompleteRegistryEntry]:
        find = name.lower()
        return Ok(_autocomplete_registry[find]) if find in _autocomplete_registry else NotFound()
