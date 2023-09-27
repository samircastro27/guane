from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Optional, TypeVar

from pydantic import BaseModel as PydanticBaseModel

CreateSchemaType = TypeVar("CreateSchemaType", bound=PydanticBaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=PydanticBaseModel)


class BaseModel(PydanticBaseModel):
    class Config:
        use_enum_values = True


class CountDB(BaseModel):
    count: int


class RangeDates(BaseModel):
    initial_date: Optional[datetime]
    final_date: Optional[datetime]


class BaseResponse(BaseModel):
    id: int
    created_at: datetime
    last_modified: datetime


class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class UserFilter(BaseModel):
    user_id: int
