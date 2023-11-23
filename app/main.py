import logging
from pathlib import Path

import sentry_sdk
from debug_toolbar.middleware import DebugToolbarMiddleware
from fastapi import FastAPI, Request, Response
from mangum import Mangum
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from starlette.middleware.cors import CORSMiddleware

# from app.api.endpoints import auth, query
from app.api.endpoints import query
from app.core.config import get_settings
from app.core.database import engine
from app.core.logger.custom_logging import CustomizeLogger
from app.models._base import Base


# loggingセットアップ
class NoParsingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.getMessage().find("/docs") >= 0


Base.metadata.create_all(
    bind=engine, checkfirst=True
)  # if you want to narrow down the tables to create, use 'tables=[models.<Class>]

# 環境変数など
settings = get_settings()

# init FastAPI
def create_app() -> FastAPI:
    app = FastAPI(
        title=f"[{settings.ENV}]{settings.TITLE}",
        version=settings.VERSION,
        debug=settings.DEBUG or False,
        # root_path=f"{settings.API_GATEWAY_STAGE_PATH}/",
    )
    # Set up custom logging
    config_path = Path(__file__).with_name(
        "logging_config.json"
        if settings.ENV != "local"
        else "logging_config_local.json"
    )
    app.logger = CustomizeLogger.make_logger(config_path)
    return app


app = create_app()


if settings.SENTRY_SDK_DNS:
    sentry_sdk.init(
        dsn=settings.SENTRY_SDK_DNS,
        integrations=[SqlalchemyIntegration()],
        environment=settings.ENV,
    )


app.add_middleware(SentryAsgiMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
    allow_origin_regex=r"^https?:\/\/([\w\-\_]{1,}\.|)example\.com",
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["info"])
def get_info(request: Request, response: Response) -> dict[str, str]:
    logger = request.app.logger
    logger.debug("The DEBUG mode is turned on.")
    return {"title": settings.TITLE, "version": settings.VERSION}


# app.include_router(auth.router, tags=["Auth"], prefix="/auth")
app.include_router(query.router, tags=["Query"], prefix="/users")

if settings.DEBUG:
    app.add_middleware(
        DebugToolbarMiddleware,
        panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
    )

if settings.IS_API_GATEWAY:
    handler = Mangum(app)
