from typing import Any

from httpx import AsyncClient

from .auth_base import IAuthBase


class AuthService:
    def __init__(self, auth: IAuthBase):
        self._auth = auth

    def decode_token(self, token: str) -> dict[str, Any]:
        return self._auth.decode_token(self, token)

    async def authenticate(
        self, username: str, password: str
    ) -> dict[str, Any]:
        return await self._auth.authenticate(self, username, password)
