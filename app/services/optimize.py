from app.services.base.base_service import BaseService
from app.core.config import settings


class OptimizeService(BaseService):
    ...


optimize_service = OptimizeService(f"{settings.LEGACY_SERVICE}api/optimize")
