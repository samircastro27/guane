from typing import Any

from app.services.base.base_service import BaseService
from app.core.config import settings
from app.schemas.case import CaseCreate


class CaseService(BaseService):
    async def get_or_create(
        self, *, obj_in: CaseCreate
    ) -> tuple[dict[str, Any], int]:
        url = f"{self.url}/get-or-create"
        response = await self._client.post(
            url_service=url,
            body=obj_in.json(exclude_none=True, exclude_unset=True),
        )
        await self._check_codes.check_codes(response=response)
        return response.json(), response.status_code

    async def create_or_update(
        self, *, obj_in: CaseCreate
    ) -> tuple[dict[str, Any], int]:
        url = f"{self.url}/create-or-update"
        response = await self._client.post(
            url_service=url,
            body=obj_in.json(exclude_none=True, exclude_unset=True),
        )
        await self._check_codes.check_codes(response=response)
        return response.json(), response.status_code


case_service = CaseService(f"{settings.DATABASE_SERVICE}api/v1/case")
