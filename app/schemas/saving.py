from enum import Enum
from typing import Optional
from datetime import date

from pydantic import BaseModel, Field, root_validator
from pydantic.error_wrappers import ValidationError, ErrorWrapper

from app.schemas import general
from app.schemas.bank import BankInDB
from app.schemas.dsaving import DsavingInDB


class SavingType(str, Enum):
    risk_free = "Risk Free"
    periodic = "Periodic"


class Status(str, Enum):
    OPEN = "Open"
    OPTION = "Option"


class RateType(str, Enum):
    EA = "e.a."
    EM = "e.m."


class SavingBase(BaseModel):
    name: str
    rate: float = Field(gt=0)
    type: SavingType
    status: Status = Status.OPTION
    rate_type: RateType = RateType.EA
    months: int = Field(None, gt=0)

    init_date: Optional[date] = None
    amount: Optional[float] = None


class SavingCreate(SavingBase):
    user_id: int

    @root_validator(pre=True)
    def root_validate(cls, values):
        if values["status"] == Status.OPEN and values["init_date"] is None:
            raise ValidationError(
                [
                    ErrorWrapper(
                        ValueError("Debes ingresas fecha de inicio"),
                        loc="init_date",
                    )
                ],
                cls,
            )
        return values


class SavingUpdate(BaseModel):
    name: Optional[str]
    rate: Optional[float]
    months: Optional[int]
    type: Optional[SavingType]
    status: Optional[Status]
    rate_type: Optional[RateType]
    amount: Optional[float]
    init_date: Optional[date]
    end_date: Optional[date]


class SavingInDB(general.BaseResponse, SavingBase):
    user_id: int


class SearchSaving(BaseModel):
    user_id: int
    status: Status = None

    class Config:
        use_enum_values = True


class GetAllReturn(BaseModel):
    total: int
    data: list[SavingInDB]


class BankMultiResponse(BankInDB):
    dsavings: list[DsavingInDB] = Field(default_factory=list)


class OptionsReturn(BaseModel):
    kyrk: list[BankMultiResponse]
    user: GetAllReturn
