from enum import StrEnum
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEV = "dev"
    CI = "ci"
    PROD = "prod"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "FinanceManager"
    app_version: str = "1.0.0"
    app_env: Environment = Environment.PROD

    # Database
    database_url: str = ""
    database_pool_size: int = 20
    database_max_overflow: int = 10
    database_use_in_memory: bool = False
    database_seed_data: str | None = None

    # CORS
    allowed_origins: list[str] = []


@lru_cache
def get_settings() -> Settings:
    return Settings()
