from typing import Any, TypeVar

from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .errors import Conflict, Invalid, NotFound
from .result import Err, Result

T = TypeVar("T")


class ProblemDetails(BaseModel):
    title: str
    status: int
    detail: str
    instance: str | None = None


def handle_error(error: Err) -> ProblemDetails:
    match error:
        case NotFound() as x:
            return ProblemDetails(
                title="Not Found", status=status.HTTP_404_NOT_FOUND, detail=x.message
            )
        case Conflict() as x:
            return ProblemDetails(
                title="Conflict", status=status.HTTP_409_CONFLICT, detail=x.message
            )
        case Invalid() as x:
            return ProblemDetails(
                title="Validation Errors",
                status=status.HTTP_400_BAD_REQUEST,
                detail=x.message,
            )
        case Err() as x:
            return ProblemDetails(
                title="Problem", status=500, detail="An unexpected problem occurred"
            )


def handle_result[T](result: Result[T]) -> T | JSONResponse:
    if result.status == "ok":
        return result.value

    problem_details = handle_error(result)
    return JSONResponse(
        status_code=problem_details.status,
        content=problem_details.model_dump(exclude_none=True),
        media_type="application/problem+json",
    )


def handled_error_responses() -> dict[int | str, dict[str, Any]]:
    return {
        status.HTTP_400_BAD_REQUEST: {"model": ProblemDetails},
        status.HTTP_404_NOT_FOUND: {"model": ProblemDetails},
        status.HTTP_409_CONFLICT: {"model": ProblemDetails},
    }
