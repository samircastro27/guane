from fastapi import HTTPException, Security, Depends, status
from fastapi.security import OAuth2PasswordBearer

from app.core import constants
from app.helpers.errors import ServiceException
from app.schemas.token import LoggedUser
from app.schemas.general import Status
from app.services import auth_service, user_service

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


async def get_current_user(
    token: str = Security(reusable_oauth2),
) -> LoggedUser:
    try:
        payload = auth_service.decode_token(token)
        user = await user_service.get_by_uid(uid=payload["uid"])
        user = LoggedUser(**payload, id=user["id"], status=user["status"])
        if user:
            return user
    except ServiceException as e:
        raise HTTPException(
            status_code=e.status_code,
            detail=constants.INVALID_CREDENTIALS_MSG + " " + e.detail
            if isinstance(e.detail, str)
            else e.detail,
        )
    raise HTTPException(status_code=404, detail=constants.USER_NOT_FOUND_MSG)


async def get_current_active_user(
    user: LoggedUser = Depends(get_current_user),
) -> LoggedUser:
    if user.status == Status.ACTIVE:
        return user
    raise HTTPException(
        status.HTTP_403_FORBIDDEN, detail=constants.INACTIVE_USER_MSG
    )
