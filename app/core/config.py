import os
from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # NOTE: .envファイルや環境変数が同名の変数にセットされる
    TITLE: str = "FastAPI App"
    ENV: str = ""
    DEBUG: bool = False
    VERSION: str = "0.0.1"
    CORS_ORIGINS: list[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://localhost:3333",
    ]
    BASE_DIR_PATH: str = str(Path(__file__).parent.parent.absolute())
    ROOT_DIR_PATH: str = str(Path(__file__).parent.parent.parent.absolute())
    SERVER_URI: str
    DATABASE_NAME: str
    DATABASE_USERNAME: str = "username"
    DATABASE_PASSWORD: str = "password"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = "secret"
    LOGGER_CONFIG_PATH: str = os.path.join(BASE_DIR_PATH, "logger_config.yaml")
    SENTRY_SDK_DNS: str = ""
    MIGRATIONS_DIR_PATH: str = os.path.join(ROOT_DIR_PATH, "alembic")
    IS_API_GATEWAY: bool = False 

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
