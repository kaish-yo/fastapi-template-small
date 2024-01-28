from logging import getLogger

from fastapi import Request
from fastapi_nextauth_jwt import NextAuthJWT

from app.core.config import get_settings

settings = get_settings()

# loggingセットアップ
logger = getLogger(__name__)

# JWTトークンの取得
JWT = NextAuthJWT(secret=settings.NEXTAUTH_SECRET)


# NextAuthにより発行されたJWTトークンを検証し、claimsを返す
async def validate_jwt_token(
    request: Request,
) -> dict:
    # ヘッダーのチェック
    logger.debug(f"{request.headers=}")

    # JWTトークンの取得
    JWT = NextAuthJWT(secret=settings.NEXTAUTH_SECRET)
    jwt_claims = JWT(request)

    # 各エンドポイントがJWTトークンの内容をrequestから参照できるようにする
    request.state.jwt_claims = jwt_claims

    return jwt_claims
