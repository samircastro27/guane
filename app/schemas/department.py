from typing import Optional

from pydantic import BaseModel

from app.schemas import general


class DepartmentInDB(general.BaseResponse):
    name: str
    state_code: str


class SearchDepartment(BaseModel):
    name: Optional[str]
