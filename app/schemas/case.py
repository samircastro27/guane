from typing import Optional

from pydantic import BaseModel, Field

from app.schemas import general


class CaseBase(BaseModel):
    T: Optional[int] = Field(default=120, gt=0)
    minimum_saving: Optional[float] = Field(default=1, gt=0)
    initial_saving: Optional[float] = 0
    prima: Optional[bool] = True
    initial_unemployment_stock: Optional[float] = 0
    tax_advance_percentage: Optional[float] = Field(1, ge=0, le=1)
    prepaid_healthcare: Optional[float] = Field(
        0.5,
        ge=0,
    )
    representation_cost: Optional[bool] = False
    AnnualTaxPaymentRate: Optional[float] = Field(7 / 100, ge=0)
    include_final_balance: Optional[bool] = True
    unemployment_independent: Optional[bool] = False
    taxAdvanceSavOpt: Optional[float] = 0.07
    annual_target_rate: Optional[float] = None
    AnnualSavInterest: Optional[float] = None


class CaseCreate(CaseBase):
    user_id: int


class CaseUpdate(CaseBase):
    ...


class CaseInDB(general.BaseResponse, CaseBase):
    class Config:
        orm_mode = True


class GetAllReturn(BaseModel):
    total: int
    data: list[CaseInDB]
