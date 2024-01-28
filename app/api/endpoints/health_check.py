from logging import getLogger

from fastapi import APIRouter, Depends, Request

from app.api.authentication import validate_jwt_token
from app.core.config import get_settings

settings = get_settings()
logger = getLogger(__name__)

router = APIRouter(dependencies=[Depends(validate_jwt_token)])


@router.get("/jwt_token")
async def return_jwt(request: Request):
    return request.state.jwt_claims


@router.get("/")
async def get_return_jwt(request: Request):
    jwt_claims = request.state.jwt_claims
    logger.debug(jwt_claims)
    return {"message": f"Hi {jwt_claims['username']}. Greetings from fastapi!"}


# For CSRF protection testing
@router.post("/")
async def post_return_jwt(request: Request):
    jwt_claims = request.state.jwt_claims
    logger.debug(jwt_claims)
    return {"message": f"Hi {jwt_claims['username']}. Greetings from fastapi!"}
