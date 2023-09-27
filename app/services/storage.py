from typing import Any

from app.services.base.base_service import BaseService
from app.core.config import settings
from app.schemas.storage import StorageCreate


class StorageService(BaseService):
    async def get_or_create(
        self, *, obj_in: StorageCreate
    ) -> tuple[dict[str, Any], int]:
        url = f"{self.url}/get-or-create"
        response = await self._client.post(
            url_service=url, body=obj_in.json(exclude_none=True)
        )
        await self._check_codes.check_codes(response=response)
        return response.json(), response.status_code

    async def create_or_update(
        self, *, obj_in: StorageCreate
    ) -> tuple[dict[str, Any], int]:
        url = f"{self.url}/create-or-update"
        response = await self._client.post(
            url_service=url, body=obj_in.json(exclude_none=True)
        )
        await self._check_codes.check_codes(response=response)
        return response.json(), response.status_code


storage_service = StorageService(f"{settings.DATABASE_SERVICE}api/v1/storage")
