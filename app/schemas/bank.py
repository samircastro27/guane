from enum import Enum
from typing import Optional

from pydantic import BaseModel

from app.schemas import general
from app.schemas.debt import DebtInDB
from app.schemas.dsaving import DsavingInDB


class BankType(str, Enum):
    CREDIT_UNIONS = "Credit Unions"
    INVESMENT = "Investment"
    COMMERCIAL = "Commercial"
    RETAIL = "Retail"
    SAVINGS_LOAN_ASSOCIATIONS = "Savings and loan associations"
    COMMUNITY_DEVELOPMENT = "Community development"
    ONLINE_NEOBANK = "Online or neobank"


class BankBase(BaseModel):
    name: str
    address: str
    phone_number: str
    type: BankType
    email: str
    nib: Optional[str]


class BankCreate(BankBase):
    ...


class BankUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    type: Optional[BankType]
    email: Optional[str]


class BankInDB(BankBase, general.BaseResponse):
    ...


class BankMultiResponse(BankInDB):
    dsavings: list[DsavingInDB] = []
    debts: list[DebtInDB] = []


class GetAllReturn(BaseModel):
    total: int
    data: list[BankMultiResponse]
