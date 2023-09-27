import json
from typing import Optional
from app.services.base.base_service import BaseService
from app.core.config import settings
from app.schemas.financial_bucket import (
    FinancialBucketCreate,
    FinancialBucketInDB,
)


class FinancialBucketService(BaseService):
    async def create(self, *, obj_in: FinancialBucketCreate):
        url = f"{self.url}"
        body = obj_in.json(exclude_none=True)
        formated_body = json.dumps(
            {k: v for k, v in json.loads(body).items() if v != []}
        )
        response = await self._client.post(url_service=url, body=formated_body)

        return response.json()

    async def delete_item(self, *, obj_in: FinancialBucketCreate):
        url = f"{self.url}{'delete/item'}"
        body = obj_in.json(exclude_none=True)
        formated_body = json.dumps(
            {k: v for k, v in json.loads(body).items() if v != []}
        )
        await self._client.post(url_service=url, body=formated_body)


financial_bucket_service = FinancialBucketService(
    f"{settings.DATABASE_SERVICE}api/v1/financial-bucket"
)
