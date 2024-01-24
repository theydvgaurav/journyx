import os

from flask import request

from common.logging.logger import logger
from utils.generate_jwt_token import decode_jwt
from .exceptions import MissingHeaderTokenException, InvalidTokenException


def authenticate():
    auth_token = request.headers.get('Authorization').split("Bearer ")[-1]
    logger.info(f"Incoming API Key : {auth_token}")
    if not auth_token:
        raise MissingHeaderTokenException
    try:
        payload = decode_jwt(auth_token, os.getenv("JWT_ADMIN_ENCODE_SECRET"), audience="JOURNYX_USER")
        if payload.get("tokenType") != "ACCESS":
            raise InvalidTokenException
        return payload.get("userId")
    except Exception as e:
        raise InvalidTokenException


def require_authentication(func):
    def wrapper(*args, **kwargs):
        user_id = authenticate()
        return func(user=user_id, *args, **kwargs)

    return wrapper
