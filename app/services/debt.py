from app.services.base.base_service import BaseService
from app.core.config import settings


class DebtService(BaseService):
    ...


debt_service = DebtService(f"{settings.DATABASE_SERVICE}api/v1/debt")
