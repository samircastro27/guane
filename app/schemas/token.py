from typing import Optional

from app.schemas.general import BaseModel, Status


class Token(BaseModel):
    access_token: str
    token_type: str


class LoggedUser(BaseModel):
    id: int
    uid: str
    email: str
    email_verified: bool
    status: Status