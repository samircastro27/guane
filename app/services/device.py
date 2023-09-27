from typing import Any

from app.services.base.base_service import BaseService
from app.core.config import settings


class DeviceService(BaseService):
    async def log_out(self, *, token: str) -> dict[str, Any]:
        url = f"{self.url}/log-out/{token}"
        response = await self._client.patch(url_service=url)
        await self._check_codes.check_codes(response=response)
        return response


device_service = DeviceService(f"{settings.DATABASE_SERVICE}api/v1/device")