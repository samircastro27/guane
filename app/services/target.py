from app.services.base.base_service import BaseService
from app.core.config import settings


class TargetService(BaseService):
    ...


target_service = TargetService(f"{settings.DATABASE_SERVICE}api/v1/target")
