from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.income import IncomeBase
from app.schemas.expenditure import ExpenditureBase
from app.schemas.saving import SavingBase
from app.schemas.target import TargetBase
from app.schemas import general


class Data(BaseModel):
    incomes: list[IncomeBase] = Field(default_factory=list)
    expenditures: list[ExpenditureBase] = Field(default_factory=list)
    savings: list[SavingBase] = Field(default_factory=list)
    targets: list[TargetBase] = Field(default_factory=list)


class StorageBase(BaseModel):
    step: Optional[int]
    data: Optional[Data]


class StorageCreate(StorageBase):
    user_id: int


class StorageInDB(general.BaseResponse, StorageBase):
    pass
