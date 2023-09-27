import logging
from typing import Any, Optional
from json import loads

from httpx._auth import Auth
from httpx._client import AsyncClient
from pydantic import AnyHttpUrl

log = logging.getLogger(__name__)


class HTTPClient:
    async def get(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 120,
        auth: Optional[Auth] = None,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, Any]] = None,
        cookies: Optional[dict[str, Any]] = None,
    ) -> Optional[dict[str, Any]]:
        try:
            async with AsyncClient() as client:
                response = await client.get(
                    url_service,
                    params=params,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )

                return response

        except Exception as e:
            log.error(e)
            return None

    async def post(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 120,
        auth: Optional[Auth] = None,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        body: Optional[dict[str, Any]] = None,
        file: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, Any]] = None,
        cookies: Optional[dict[str, Any]] = None,
        xml: Optional[bool] = False,
    ) -> Optional[dict[str, Any]]:
        try:
            async with AsyncClient() as client:
                response = await client.post(
                    url_service,
                    params=params,
                    json=loads(body),
                    data=data,
                    files=file,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

    async def put(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 120,
        auth: Optional[Auth] = None,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, Any]] = None,
        cookies: Optional[dict[str, Any]] = None,
    ) -> Optional[dict[str, Any]]:
        try:
            async with AsyncClient() as client:
                response = await client.put(
                    url_service,
                    params=params,
                    json=body,
                    data=data,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

    async def delete(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 120,
        auth: Optional[Auth] = None,
        headers: Optional[dict[str, Any]] = None,
        cookies: Optional[dict[str, Any]] = None,
        params: Optional[dict[str, Any]] = None,
    ) -> Optional[dict[str, Any]]:
        try:
            async with AsyncClient() as client:
                response = await client.delete(
                    url_service,
                    params=params,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None

    async def patch(
        self,
        *,
        url_service: AnyHttpUrl,
        timeout: float = 120,
        auth: Optional[Auth] = None,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        body: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, Any]] = None,
        cookies: Optional[dict[str, Any]] = None,
    ) -> Optional[dict[str, Any]]:
        try:
            async with AsyncClient() as client:
                body = body if isinstance(body, dict) else loads(body)
                response = await client.patch(
                    url_service,
                    params=params,
                    json=body,
                    data=data,
                    headers=headers,
                    cookies=cookies,
                    timeout=timeout,
                    auth=auth,
                )
                return response
        except Exception as e:
            log.error(e)
            return None
