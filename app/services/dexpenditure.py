from app.services.base.base_service import BaseService
from app.core.config import settings


class DexpenditureService(BaseService):
    ...


dexpenditure_service = DexpenditureService(f"{settings.DATABASE_SERVICE}api/v1/dexpenditure")
