import logging
from datetime import datetime

from httpx._models import Response

from app.core.config import settings
from app.helpers.errors import ServiceException

ES = settings.EXCEPTIONS["es"]
EN = settings.EXCEPTIONS["en"]

logger = logging.getLogger(__name__)


class Responses:
    def __init__(self):
        self.code_switcher = {
            400: self.__400,
            401: self.__401,
            403: self.__403,
            404: self.__404,
            409: self.__409,
            422: self.__422,
            500: self.__500,
        }

    def __400(self):
        return [{"es": ES[400], "en": EN[400]}]

    def __401(self):
        return [{"es": ES[401], "en": EN[401]}]

    def __403(self):
        return [{"es": ES[403], "en": EN[403]}]

    def __404(self):
        return [{"es": ES[404], "en": EN[404]}]
    
    def __409(self):
        return [{"es": ES[409], "en": EN[409]}]

    def __422(self):
        return [{"es": ES[422], "en": EN[422]}]

    def __500(self):
        return [{"es": ES[500], "en": EN[500]}]

    async def check_codes(self, *, response: Response, delete_method=False):
        if not response:
            raise ServiceException(
                status_code=500,
                detail={
                    "errors": [{"es": ES[500], "en": EN[500]}],
                },
            )
        code = self.code_switcher.get(response.status_code, lambda: None)
        content = code()
        if content:
            content += [{"description": response.json().get("detail", "")}]
            raise ServiceException(
                status_code=response.status_code, detail=content
            )
