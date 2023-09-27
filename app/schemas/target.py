import datetime
from typing import Optional

from pydantic import BaseModel

from app.schemas import general
from app.schemas.category import Category


class TargetBase(BaseModel):
    name: str
    amount: float
    unemployment_insurance: Optional[bool] = False
    inflation: Optional[bool] = False
    expected_date: datetime.date
    initial: float = 0
    category: Optional[Category] = Category.OTHER


class TargetCreate(TargetBase):
    user_id: int


class TargetUpdate(BaseModel):
    name: Optional[str]
    amount: Optional[float]
    unemployment_insurance: Optional[bool] = False
    inflation: Optional[bool] = False
    expected_date: Optional[datetime.date]
    initial: Optional[float] = 0


class TargetInDB(general.BaseResponse, TargetCreate):
    amount_inflation: Optional[float]
    user_id: int


class GetAllReturn(BaseModel):
    total: int
    data: list[TargetInDB]
