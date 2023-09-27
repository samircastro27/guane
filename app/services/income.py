from typing import Optional, Any

from app.services.base.base_service import BaseService
from app.core.config import settings


class IncomeService(BaseService):
    ...


income_service = IncomeService(f"{settings.DATABASE_SERVICE}api/v1/income")
