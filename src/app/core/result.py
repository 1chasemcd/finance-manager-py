from dataclasses import dataclass
from typing import Literal, TypeVar

T = TypeVar("T", default=None)


@dataclass(frozen=True)
class Ok[T]:
    value: T
    status: Literal["ok"] = "ok"


class NoContent(Ok[None]):
    def __init__(self) -> None:
        super().__init__(value=None)


@dataclass(frozen=True)
class Err:
    status: Literal["err"] = "err"


Result = Ok[T] | Err
