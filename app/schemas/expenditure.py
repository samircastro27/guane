from enum import Enum
from typing import Optional, Any
import datetime
from wsgiref.validate import ErrorWrapper

from pydantic import BaseModel, Field, ValidationError, validator
from random import randint
from app.schemas import general
from app.schemas.category import Category


class ExpenditureType(str, Enum):
    single = "single"
    recurrent = "recurrent"
    fixed = "fixed"


class ExpenditureBase(BaseModel):
    name: str
    type: ExpenditureType
    amount: float = Field(..., ge=0)
    notify: Optional[bool] = None
    notification_day: Optional[str] = Field(default="0-0")
    frequency: Optional[int] = Field(1, ge=1)
    date: Optional[datetime.date] = None
    inflation: Optional[bool] = None
    end_date: Optional[datetime.date] = None
    category: Optional[Category] = Category.OTHER


class ExpenditureValidation(ExpenditureBase):
    @validator("end_date")
    def end_date_gt_date(
        cls, v: Optional[datetime.date], values: dict[str, Any]
    ):
        if v and v < values["date"]:
            raise ValueError("Expenditure date is larger than its end_date")
        if v is None and values.get("type") == ExpenditureType.recurrent:
            raise ValueError("Expenditure recurrent need end_date")
        return v

    @validator("notification_day")
    def generate_random_notification_day(cls, v: str) -> int:
        if not v:
            return 0
        if v and "-" in v:
            range_start, range_end = map(int, v.split("-"))
            if range_start > range_end:
                range_start, range_end = range_end, range_start
            return randint(range_start, range_end)
        raise ValidationError(
            [
                ErrorWrapper(
                    ValueError("Invalid range format for notification_day"),
                    loc="bonuses",
                )
            ],
            cls,
        )


class ExpenditureCreate(ExpenditureValidation):
    user_id: int


class ExpenditureUpdate(ExpenditureValidation):
    name: Optional[str] = None
    type: Optional[ExpenditureType] = None
    amount: Optional[float] = Field(None, ge=0)


class ExpenditureInDB(general.BaseResponse, ExpenditureBase):
    notification_day: str
    user_id: int


class SearchExpenditure(BaseModel):
    user_id: int


class GetAllReturn(BaseModel):
    total: int
    data: list[ExpenditureInDB]
