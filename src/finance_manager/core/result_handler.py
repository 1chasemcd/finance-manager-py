from fastapi.responses import JSONResponse
from pydantic import BaseModel

from finance_manager.core.errors import Conflict, Invalid, NotFound
from finance_manager.core.result import Err, Result


class ProblemDetails(BaseModel):
    title: str
    status: int
    detail: str
    instance: str | None = None


class ValidationProblemDetails(ProblemDetails):
    errors: dict[str, list[str]]


def handle_error(error: Err) -> ProblemDetails | ValidationProblemDetails:
    match error:
        case NotFound() as x:
            return ProblemDetails(title="Not Found", status=404, detail=x.message)
        case Conflict() as x:
            return ProblemDetails(title="Conflict", status=409, detail=x.message)
        case Invalid() as x:
            return ValidationProblemDetails(
                title="Validation Errors",
                status=400,
                detail=x.message,
                errors=x.errors if x.errors else {},
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
