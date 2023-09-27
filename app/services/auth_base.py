from typing import Any

from abc import ABC, abstractmethod


class IAuthBase(ABC):
    @abstractmethod
    def decode_token(self, token: str) -> dict[str, Any]:
        """method to decode a token"""
    
    async def authenticate(self, username: str, password: str) -> dict[str, Any]:
        """method to auth an user"""