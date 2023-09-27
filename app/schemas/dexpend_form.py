from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field

from app.schemas import general
from app.schemas.expenditure import ExpenditureInDB


class HousingType(str, Enum):
    RENT = "RENT"
    OWN = "OWN"
    FAMILY = "FAMILY"


class AgeRange(str, Enum):
    LE25 = "LE25"
    FROM25TO35 = "FROM 25 TO 35"
    FROM35TO45 = "FROM 35 TO 45"
    GE45 = "GE45"


class DExpendFormBase(BaseModel):
    housing_type: Optional[HousingType] = HousingType.RENT
    age_range: Optional[AgeRange] = None
    has_children: Optional[bool] = None
    owns_vehicle: Optional[bool] = None


class DExpendFormCreate(DExpendFormBase):
    user_id: int


class DExpendFormUpdate(DExpendFormBase):
    housing_type: Optional[HousingType] = HousingType.RENT
    age_range: Optional[AgeRange] = None
    has_children: Optional[bool] = None
    owns_vehicle: Optional[bool] = None


class DExpendFormInDB(general.BaseResponse, DExpendFormBase):
    ...


class DExpendFormResponse(general.BaseResponse, DExpendFormBase):
    expenditures: list[ExpenditureInDB] = Field(default_factory=list)
