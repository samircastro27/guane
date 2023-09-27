from typing import Optional, Any
from enum import Enum
import datetime

from pydantic import BaseModel, Field, validator
from pydantic.error_wrappers import ValidationError, ErrorWrapper

from app.schemas import general
from app.schemas.bank import BankInDB
from app.schemas.debt import DebtInDB


class LoanType(str, Enum):
    SIMPLE = "Simple"
    MORTGAGE = "Mortgage"
    OPTION = "Option"


class RateType(str, Enum):
    EA = "e.a."
    EM = "e.m."


class LoanTypeExtended(str, Enum):
    SIMPLE = "Simple"
    MORTGAGE = "Mortgage"
    OPTION = "Option"
    SIMPLEANDMORTGAGES = "Simple and Mortgages"



class LoanBase(BaseModel):
    name: str
    rate: float = Field(ge=0)
    rate_type: RateType

    date: Optional[datetime.date] = None
    months: Optional[int] = Field(ge=1)
    amount: Optional[float] = Field(ge=0)
    type: Optional[LoanType] = LoanType.OPTION


class LoanCreate(LoanBase):
    user_id: int
    existent: Optional[bool] = None

    @validator("existent", always=True)
    def _existent(cls, v: Optional[bool], values: dict[str, Any]):
        print(values.get("date"), "None")
        if values.get("date", None) is not None:
            return values.get("date") < datetime.date.today()
        return False


class LoanUpdate(BaseModel):
    name: Optional[str]
    amount: Optional[float] = Field(ge=0)
    rate: Optional[float] = Field(ge=0)
    months: Optional[int] = Field(ge=1)
    existent: Optional[bool]
    type: Optional[LoanType]
    rate_type: Optional[RateType]
    date: Optional[datetime.date]


class LoanInDB(general.BaseResponse, LoanBase):
    user_id: int
    existent: Optional[bool] = None


class SearchLoan(BaseModel):
    user_id: int
    type: LoanTypeExtended = None

    class Config:
        use_enum_values = True


class GetAllReturn(BaseModel):
    total: int
    data: list[LoanInDB]


class BankMultiResponse(BankInDB):
    debts: list[DebtInDB] = Field(default_factory=list)


class OptionsReturn(BaseModel):
    kyrk: list[BankMultiResponse]
    user: GetAllReturn
