from typing import Any

from app.services.base.base_service import BaseService
from app.services.optimize import optimize_service
from app.core.config import settings
from app.schemas.plandetail import PlanDetailDTO
from app.schemas.plan import PlanFullCreate, PlanFollow
from app.schemas.optimize import OptimizeQueue


class PlanService(BaseService):
    async def create_details(
        self, *, obj_in: PlanDetailDTO
    ) -> dict[str, Any]:
        url = f"{self.url}/details"
        response = await self._client.post(
            url_service=url, body=obj_in.json(exclude_none=True)
        )
        await self._check_codes.check_codes(response=response)
        if response.status_code == 201:
            await optimize_service.create(
                obj_in=OptimizeQueue(id=response.json()["id"]), route="/queue"
            )
        return response.json()

    async def get_detailed(self, *, id: int) -> dict[str, Any]:
        url = f"{self.url}/{id}/detailed"
        response = await self._client.get(url_service=url)
        await self._check_codes.check_codes(response=response)
        return response.json()

    async def full_create(self, *, obj_in: PlanFullCreate) -> dict[str, Any]:
        url = f"{self.url}/full-create"
        response = await self._client.post(
            url_service=url, body=obj_in.json(exclude_none=True)
        )
        await self._check_codes.check_codes(response=response)
        if response.status_code == 201:
            await optimize_service.create(
                obj_in=OptimizeQueue(id=response.json()["id"]), route="/queue"
            )
        return response.json()

    async def follow_plan(
        self, *, id: int, obj_in: PlanFollow
    ) -> dict[str, Any]:
        url = f"{self.url}/{id}/follow"
        response = await self._client.patch(
            url_service=url, body=obj_in.dict(exclude_none=True)
        )
        await self._check_codes.check_codes(response=response)
        return response


plan_service = PlanService(f"{settings.DATABASE_SERVICE}api/v1/plan")
