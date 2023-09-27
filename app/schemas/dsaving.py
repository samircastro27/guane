from enum import Enum
from typing import Optional, Any

from pydantic import BaseModel

from app.schemas import general


class DsavingType(str, Enum):
    risk_free = "Risk Free"
    periodic = "Periodic"


class DsavingBase(BaseModel):
    name: str
    rate: float
    months: int
    type: DsavingType


class DsavingCreate(DsavingBase):
    bank_id: int


class DsavingUpdate(BaseModel):
    name: Optional[str]
    rate: Optional[float]
    months: Optional[int]
    type: Optional[DsavingType]


class DsavingInDB(general.BaseResponse, DsavingBase):
    ...


class DsavingMultiResponse(DsavingInDB):
    bank: Any


class GetAllReturn(BaseModel):
    total: int
    data: list[DsavingMultiResponse]
