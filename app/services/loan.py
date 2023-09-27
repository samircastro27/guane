from typing import Any, Optional

from app.services.base.base_service import BaseService
from app.core.config import settings


class LoanService(BaseService):
    async def options(
        self,
        *,
        payload: Optional[dict[str, Any]] = None,
        skip: int = 0,
        limit: int = 1000,
    ) -> dict[str, Any]:
        return await super().get_all(payload, skip, limit, "/options")


loan_service = LoanService(f"{settings.DATABASE_SERVICE}api/v1/loan")
