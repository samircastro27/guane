from typing import Any

from firebase_admin import auth
from httpx._client import AsyncClient

from app.helpers.errors import ServiceException
from app.services.auth_base import IAuthBase
from app.core.config import settings
from .app import app


class AuthFireBase(IAuthBase):
    def decode_token(self, token: str) -> dict[str, Any]:
        try:
            return auth.verify_id_token(token, app)
        except (
            auth.InvalidIdTokenError,
            auth.ExpiredIdTokenError,
            auth.RevokedIdTokenError,
            auth.CertificateFetchError,
            auth.UserDisabledError,
        ) as e:
            raise ServiceException(401, str(e))

    async def authenticate(
        self, username: str, password: str
    ) -> dict[str, Any]:
        async with AsyncClient() as client:
            body = {
                "email": username,
                "password": password,
                "returnSecureToken": True
            }
            params = {"key": settings.API_FIREBASE_KEY}
            response = await client.post(
                settings.API_FIREBASE_URL,
                json=body,
                params=params,
                timeout=120,
            )
            return response.json()
