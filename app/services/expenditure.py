from typing import Optional, Any

from app.services.base.base_service import BaseService
from app.core.config import settings


class ExpenditureService(BaseService):
    ...


expenditure_service = ExpenditureService(f"{settings.DATABASE_SERVICE}api/v1/expenditure")
