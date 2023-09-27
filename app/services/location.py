from app.services.base.base_service import BaseService
from app.core.config import settings


class LocationService(BaseService):
    ...


location_service = LocationService(f"{settings.DATABASE_SERVICE}api/v1/location")