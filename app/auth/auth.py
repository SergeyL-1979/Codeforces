import os

from fastapi_users.authentication import CookieTransport
from fastapi_users.authentication import JWTStrategy

from dotenv import load_dotenv

load_dotenv(override=True)

cookie_transport = CookieTransport(cookie_max_age=3600)


SECRET = os.getenv("SECRET")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)
