from typing import Optional

from pydantic import BaseModel

from app.schemas import general
from app.schemas.department import DepartmentInDB


class CityInDB(general.BaseResponse):
    name: str
    department_id: int


class SearchCity(BaseModel):
    name: Optional[str]


class CityEmbedded(CityInDB):
    department: DepartmentInDB