from typing import Any, Dict, Optional, TypeVar
from json import loads

from pydantic.main import BaseModel

from app.infra.httpx.client import HTTPClient
from app.services.base.base import IServiceBase
from app.services.base.responses import Responses

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(IServiceBase[CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        url: str,
        check_codes: Responses = Responses(),
        client: HTTPClient = HTTPClient(),
    ):
        self.url = url
        self._client = client
        self._check_codes = check_codes

    async def create(
        self, *, obj_in: CreateSchemaType, route: Optional[str] = ""
    ) -> Any:
        url = f"{self.url}{route}"
        body = obj_in.json(exclude_none=True)
        response = await self._client.post(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def update(
        self, *, _id: int, obj_in: UpdateSchemaType, route: Optional[str] = ""
    ) -> Any:
        url = f"{self.url}{route}/{_id}"
        body = obj_in.json(exclude_none=True)
        response = await self._client.patch(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        return response

    async def delete(self, *, _id: int, route: Optional[str] = "") -> Any:
        url = f"{self.url}{route}/{_id}"
        response = await self._client.delete(url_service=url)
        await self._check_codes.check_codes(
            response=response, delete_method=True
        )
        return response

    async def get_by_id(self, *, _id: int, route: Optional[str] = "") -> Any:
        url = f"{self.url}{route}/{_id}"
        response = await self._client.get(url_service=url)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def get_all(
        self,
        payload: Optional[Dict[str, Any]] = None,
        skip: int = 0,
        limit: int = 1000,
        route: Optional[str] = "",
    ) -> Any:
        if payload:
            payload.update({"skip": skip, "limit": limit})
        else:
            payload = {"skip": skip, "limit": limit}
        url = f"{self.url}{route}"
        response = await self._client.get(url_service=url, params=payload)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response
    

    async def count(
        self,
        payload: Dict[str, Any] = {},
        route: Optional[str] = "",
    ) -> Dict[str, Any]:
        url = f"{self.url}{route}"
        response = await self._client.get(url_service=url, params=payload)
        await self._check_codes.check_codes(response=response)
        return response.json()
