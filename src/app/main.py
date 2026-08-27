from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.route_processor import get_route_processor
from app.api.routes import (
    autocomplete,
    category_patterns,
    import_defs,
    people,
    transaction_categories,
    transaction_sources,
    transactions,
)
from app.config import get_settings
from app.dependencies.database import sessionmanager


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    settings = get_settings()

    # Startup
    await sessionmanager.init(settings)
    yield

    # Shutdown
    await sessionmanager.close()


def create_app() -> FastAPI:
    settings = get_settings()
    route_processor = get_route_processor()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs" if settings.app_env == "dev" else None,
        redoc_url="/redoc" if settings.app_env == "dev" else None,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(people.router)
    app.include_router(transactions.router)
    app.include_router(transaction_sources.router)
    app.include_router(transaction_categories.router)
    app.include_router(category_patterns.router)
    app.include_router(import_defs.router)
    app.include_router(autocomplete.router)
    route_processor.process_routes(app.routes)

    return app


app = create_app()
