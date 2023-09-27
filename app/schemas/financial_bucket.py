from typing import List, Optional
from pydantic import BaseModel, Field

from app.schemas import (
    expenditure,
    income,
    loan,
    saving,
    target,
    financial_income,
)


class FinancialBucketCreate(BaseModel):
    user_id: Optional[int]
    income_ids: Optional[List[int]] = Field(min_items=1, default_factory=list)
    expenditure_ids: Optional[List[int]] = Field(default_factory=list)
    saving_ids: Optional[List[int]] = Field(default_factory=list)
    target_ids: Optional[List[int]] = Field(default_factory=list)
    loan_ids: Optional[List[int]] = Field(default_factory=list)


class FinancialBucketInDB(BaseModel):
    incomes: list[financial_income.IncomeResponse] = Field(
        default_factory=list
    )
    expenditures: list[expenditure.ExpenditureInDB] = Field(
        default_factory=list
    )
    savings: list[saving.SavingInDB] = Field(default_factory=list)
    targets: list[target.TargetInDB] = Field(default_factory=list)
    loans: list[loan.LoanInDB] = Field(default_factory=list)

    class Config:
        orm_mode = True
