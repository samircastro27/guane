import datetime
from enum import Enum
from typing import Any, Optional, Union

from pydantic import BaseModel, Field, validator

from app.schemas import general
from app.schemas.bonus import BonusBase


class IncomeType(str, Enum):
    single = "single"
    recurrent = "recurrent"
    salary = "salary"


class IncomeBase(BaseModel):
    name: str
    type: IncomeType
    amount: float = Field(..., ge=0)

    frequency: Optional[int] = Field(1, ge=1)
    date: Optional[datetime.date] = None
    inflation: Optional[bool] = False
    end_date: Optional[datetime.date] = None

    @validator("end_date")
    def end_date_gt_date(cls, v, values):
        if v and v < values["date"]:
            raise ValueError("Income date is larger than its end_date")
        return v


class IncomeCreate(IncomeBase):
    user_id: int

    default_prima: Optional[bool] = True
    bonuses: Optional[list[BonusBase]] = Field(default_factory=list)


class IncomeUpdate(BaseModel):
    name: Optional[str]
    type: Optional[IncomeType]
    amount: Optional[float] = Field(0, ge=0)

    frequency: Optional[int] = Field(1, ge=1)
    date: Optional[datetime.date] = None
    inflation: Optional[bool] = False
    end_date: Optional[datetime.date] = None
    bonuses: Optional[list[BonusBase]] = None

    @validator("end_date")
    def end_date_gt_date(cls, v, values):
        if v and v < values["date"]:
            raise ValueError("Income date is larger than its end_date")
        return v


class IncomeInDB(general.BaseResponse, IncomeBase):
    user_id: int

    class Config:
        orm_mode = True


class IncomeResponse(IncomeInDB):
    bonuses: Union[Optional[list[BonusBase]], Any] = Field(
        default_factory=list
    )


class GetAllReturn(BaseModel):
    total: int
    data: list[IncomeResponse]
