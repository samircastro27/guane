from pydantic import BaseModel, Field

from app.schemas import income, expenditure, saving, loan, target


class PlanDetailCreate(BaseModel):
    income_ids: list[int] = Field(min_items=1)
    expenditure_ids: list[int] = Field(default_factory=list)
    saving_ids: list[int] = Field(default_factory=list)
    target_ids: list[int] = Field(default_factory=list)
    loan_ids: list[int] = Field(default_factory=list)


class PlanDetailDTO(PlanDetailCreate):
    user_id: int


class PlanDetailInDB(BaseModel):
    incomes: list[income.IncomeInDB] = Field(default_factory=list)
    expenditures: list[expenditure.ExpenditureInDB] = Field(default_factory=list)
    savings: list[saving.SavingInDB] = Field(default_factory=list)
    targets: list[target.TargetInDB] = Field(default_factory=list)
    loans: list[loan.LoanInDB] = Field(default_factory=list)