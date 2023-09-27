from typing import Optional
from enum import Enum

from pydantic import BaseModel

from app.schemas import general
from app.schemas.category import Category
from app.schemas.expenditure import ExpenditureType
from app.schemas.dexpend_form import HousingType, AgeRange


class DexpenditureBase(BaseModel):
    name: str
    type: ExpenditureType
    amount_lower_bound: float
    amount_upper_bound: float
    inflation: bool
    frecuency: int
    category: Category

    housing_type: Optional[HousingType] = HousingType.RENT
    age_ranges: Optional[list[AgeRange]] = None
    has_children: Optional[bool] = None
    owns_vehicle: Optional[bool] = None
    all_users: Optional[bool] = None


class DexpenditureCreate(DexpenditureBase):
    ...


class DexpenditureUpdate(BaseModel):
    name: Optional[str]
    type: Optional[ExpenditureType]
    amount_lower_bound: Optional[float]
    amount_upper_bound: Optional[float]
    inflation: Optional[bool]
    frecuency: Optional[int]
    category: Optional[Category]

    housing_type: Optional[list[AgeRange]] = HousingType.RENT
    age_range: Optional[HousingType] = None
    has_children: Optional[bool] = None
    owns_vehicle: Optional[bool] = None


class DexpenditureInDB(general.BaseResponse, DexpenditureBase):
    ...


class GetAllReturn(BaseModel):
    total: int
    data: list[DexpenditureInDB]
