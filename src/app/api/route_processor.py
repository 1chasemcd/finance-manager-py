from fastapi.routing import APIRoute
from starlette import routing

from app.core.string_utils import snake_to_camel


class RouteProcessor:
    def __init__(self) -> None:
        self.route_ids = set[str]()

    def process_routes(self, routes: list[routing.BaseRoute]) -> None:
        self._set_operation_ids(routes)

    def _set_operation_ids(self, routes: list[routing.BaseRoute]) -> None:
        for route in routes:
            if isinstance(route, APIRoute):
                id = snake_to_camel(route.endpoint.__name__)
                if id in self.route_ids:
                    raise ValueError(f"Duplicate openapi operation_id {id}")
                route.operation_id = id

            elif hasattr(route, "original_router"):
                self._set_operation_ids(route.original_router.routes)  # type: ignore


def get_route_processor() -> RouteProcessor:
    return RouteProcessor()
