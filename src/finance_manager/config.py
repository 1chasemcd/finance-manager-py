from collections.abc import Awaitable, Callable
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.ext.asyncio import AsyncSession

from finance_manager.db.seed import seed


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "FinanceManager"
    app_version: str = "1.0.0"
    debug: bool = True

    # Database
    database_url: str = "sqlite+aiosqlite:///:memory:"
    database_pool_size: int = 20
    database_max_overflow: int = 10
    database_use_in_memory: bool = True
    database_seed: Callable[[AsyncSession], Awaitable[None]] = seed

    # CORS
    allowed_origins: list[str] = ["http://localhost:3000"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
