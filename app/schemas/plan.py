from typing import Optional
from enum import Enum
from datetime import date

from pydantic import BaseModel, Field

from app.schemas import general, plandetail
from app.schemas.income import IncomeBase, IncomeCreate
from app.schemas.expenditure import ExpenditureCreate, ExpenditureBase
from app.schemas.saving import SavingCreate, SavingBase
from app.schemas.target import TargetCreate, TargetBase
from app.schemas.loan import LoanCreate, LoanBase


class PlanStatus(str, Enum):
    CREATED = "Plan recibido"
    UPDATED = "Plan actualizado"
    INQUEUE = "En lista de espera"
    PROCESSING = "Procesando"
    SUCCESS = "Completado"
    UNFEASIBLE = "Inviable"


class PlanBase(BaseModel):
    name: Optional[str] = "Plan de ahorros"
    status: Optional[PlanStatus] = PlanStatus.CREATED
    follow: Optional[bool] = False


class PlanCreate(PlanBase):
    user_id: int


class PlanUpdate(BaseModel):
    name: Optional[str]


class PlanInDB(general.BaseResponse, PlanCreate):
    init_date: Optional[date] = None
    end_date: Optional[date] = None


class PlanFullCreate(PlanCreate):
    incomes: list[IncomeCreate] = Field(default_factory=list)
    expenditures: list[ExpenditureCreate] = Field(default_factory=list)
    savings: list[SavingCreate] = Field(default_factory=list)
    targets: list[TargetCreate] = Field(default_factory=list)
    loans: list[LoanCreate] = Field(default_factory=list)

    def __init__(
        self,
        user_id: int,
        incomes: list[IncomeBase],
        expenditures: list[ExpenditureBase],
        savings: list[SavingBase],
        targets: list[TargetBase],
        loans: list[LoanBase],
        **kwargs
    ):
        super().__init__(user_id=user_id, **kwargs)
        self.incomes = [
            IncomeCreate(**income.dict(), user_id=user_id)
            for income in incomes
        ]
        self.expenditures = [
            ExpenditureCreate(**expenditure.dict(), user_id=user_id)
            for expenditure in expenditures
        ]
        self.savings = [
            SavingCreate(**saving.dict(), user_id=user_id)
            for saving in savings
        ]
        self.targets = [
            TargetCreate(**target.dict(), user_id=user_id)
            for target in targets
        ]
        self.loans = [
            LoanCreate(**loan.dict(), user_id=user_id) for loan in loans
        ]


class PlanDetailed(general.BaseResponse, PlanCreate):
    init_date: Optional[date] = None
    end_date: Optional[date] = None
    details: Optional[plandetail.PlanDetailInDB]


class PlanFollow(BaseModel):
    user_id: int


class SearchPlan(BaseModel):
    user_id: int


class ResultQuery(BaseModel):
    year: Optional[str]
    month: Optional[str]


class GetAllReturn(BaseModel):
    total: int
    data: list[PlanInDB]
