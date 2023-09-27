from pydantic import BaseModel

from app.schemas import general


class DeviceBase(BaseModel):
    token: str
    logged: bool = True


class DeviceCreate(DeviceBase):
    user_id: int


class DeviceUpdate(BaseModel):
    token: str = None
    logged: bool = True


class DeviceInDB(general.BaseResponse, DeviceCreate):
    class Config:
        orm_mode = True


class SearchDevice(BaseModel):
    user_id: int


class GetAllReturn(BaseModel):
    total: int
    data: list[DeviceInDB]
