from typing import Optional
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, Field

from app.schemas import general
from app.schemas.city import CityEmbedded


class UserOcupation(str, Enum):
    EMPLOYEE = "Empleado"
    INDEPENDENT = "Trabajador independiente"
    INFORMAL = "Empleado informal"
    ESTUDENT = "Estudiante universitario"
    UNEMPLOYED = "Desempleado"
    OTHER = "Otro"


class UserBase(BaseModel):
    uid: str
    email: EmailStr
    name: Optional[str]
    photo_url: Optional[str]
    status: general.Status
    age: Optional[int]
    city_id: Optional[int]
    other_city: Optional[str]
    phone_number: Optional[str]
    ocupation: UserOcupation
    bank: Optional[str]


class UserCreate(UserBase):
    status: Optional[general.Status] = general.Status.ACTIVE


class UserUpdate(BaseModel):
    age: Optional[int]
    name: Optional[str]
    email: Optional[EmailStr]
    status: Optional[general.Status]
    photo_url: Optional[str]
    city_id: Optional[int]
    other_city: Optional[str]
    ocupation: Optional[UserOcupation]
    phone_number: Optional[str]
    bank: Optional[str]


class UserSearch(BaseModel):
    name__icontains: Optional[str] = Field(None, alias="name")
    email__icontains: Optional[str] = Field(None, alias="email")
    city__name__icontains: Optional[str] = Field(None, alias="city_name")
    city_id: Optional[int]
    status: Optional[general.Status]

    class Config:
        allow_population_by_field_name = True


class UserInDB(general.BaseResponse, UserBase, UserUpdate):
    ...


class UserResponse(UserInDB):
    city: Optional[CityEmbedded]


class GetAllReturn(BaseModel):
    total: int
    data: list[UserInDB]
