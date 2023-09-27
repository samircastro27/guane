from enum import Enum
from typing import Optional, Any

from pydantic import BaseModel, Field, root_validator, ValidationError
from pydantic.error_wrappers import ErrorWrapper


class BonusType(str, Enum):
    BONUS = "Bonus"
    PRIMA = "Prima"


class BonusBase(BaseModel):
    name: str
    month: int = Field(gt=0, le=12)
    type: BonusType

    percentage: Optional[int] = Field(gt=0, le=100)
    amount: Optional[float] = Field(gt=0)

    @root_validator(pre=False)
    def check_nones(cls, values: dict[str, Any]):
        if not (values.get("percentage", None) or values.get("amount", None)):
            raise ValidationError(
                [
                    ErrorWrapper(
                        ValueError("amount and percentage None"),
                        loc="percentage, amount",
                    )
                ],
                cls,
            )
        return values


class BonusCreate(BonusBase):
    income_id: int


class BonusUpdate(BaseModel):
    name: Optional[str]
    month: Optional[int]
    type: Optional[BonusType]
    percentage: Optional[int]
    amount: Optional[float]


class BonusInDB(BonusBase):
    income_id: int
