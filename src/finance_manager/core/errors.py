from dataclasses import dataclass

from .result import Err


@dataclass(frozen=True)
class NotFound(Err):
    message: str = "The specified resource could not be found."


@dataclass(frozen=True)
class Conflict(Err):
    message: str = "The request conflicts with the current state of the resource."


@dataclass(frozen=True)
class Invalid(Err):
    message: str = "The request was invalid."
