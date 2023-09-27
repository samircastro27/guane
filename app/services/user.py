from typing import Optional, Any

from app.services.base.base_service import BaseService
from app.core.config import settings


class UserService(BaseService):
    async def get_by_uid(
        self,
        *,
        uid: str,
    ) -> Optional[dict[str, Any]]:
        url = f"{self.url}/uid/{uid}"
        response = await self._client.get(url_service=url)
        await self._check_codes.check_codes(response=response)
        return response.json()


user_service = UserService(f"{settings.DATABASE_SERVICE}api/v1/user")
