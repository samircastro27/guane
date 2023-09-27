from app.services.base.base_service import BaseService
from app.core.config import settings


class DsavingService(BaseService):
    ...


dsaving_service = DsavingService(f"{settings.DATABASE_SERVICE}api/v1/dsaving")
