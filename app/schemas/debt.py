from enum import Enum
from typing import Optional, Any

from pydantic import BaseModel

from app.schemas import general


class RateType(str, Enum):
    EA = "e.a."
    EM = "e.m."


class DebtBase(BaseModel):
    name: str
    months: int
    rate: float
    rate_type: RateType = RateType.EA


class DebtCreate(DebtBase):
    bank_id: int


class DebtUpdate(BaseModel):
    name: Optional[str]
    months: Optional[int]
    rate: Optional[float]
    rate_type: Optional[RateType]


class DebtInDB(general.BaseResponse, DebtBase):
    ...


class DebtMultiResponse(DebtInDB):
    bank: Any


class GetAllReturn(BaseModel):
    total: int
    data: list[DebtMultiResponse]
