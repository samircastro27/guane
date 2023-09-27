from typing import Optional, Any

from app.services.base.base_service import BaseService
from app.core.config import settings
from app.helpers.get import get


class ResultsService(BaseService):
    async def get_by_id(
        self,
        *,
        _id: int,
        route: Optional[str] = "",
        params: Optional[dict[str, Any]] = None,
    ) -> Any:
        url = f"{self.url}{route}/{_id}"
        response = await self._client.get(url_service=url, params=params)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        kpis = get(response, f"data.kpis")
        result = (
            get(
                response,
                f"data.output.{params.get('year', None)}.{params.get('month', None)}",
            )
            if params.get("year", None) is not None
            else response
        )
        result.update({"kpis": kpis}) if params.get(
            "year", None
        ) is not None else None
        return result

    async def get_stocks_by(self, *, year: str, id: int) -> Any:
        url = f"{self.url}/plan/{id}/stocks"
        response = await self._client.get(
            url_service=url, params={"year": year}
        )
        await self._check_codes.check_codes(response=response)
        return response.json()


results_service = ResultsService(f"{settings.RESULTS_SERVICE}api/results")
