from app.services.base.base_service import BaseService
from app.core.config import settings


class BankService(BaseService):
    ...


bank_service = BankService(f"{settings.DATABASE_SERVICE}api/v1/bank")
