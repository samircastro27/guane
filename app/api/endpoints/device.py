from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.device import (
    DeviceInDB,
    DeviceBase,
    DeviceCreate,
    DeviceUpdate,
    SearchDevice,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.device import device_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.DEVICES_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Devices.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchDevice`

    Returns
    -------
    List: `Device`
        List All Devices from the database.
    """
    try:
        return await device_service.get_all(
            skip=skip,
            limit=limit,
            payload=SearchDevice(user_id=current_user.id).dict(),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=DeviceInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.DEVICE_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_device: DeviceBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DeviceInDB:
    """
    Create Device.


    Create an Device in the database.

    Parameters
    ----------
    new_device: Schema `CreateDevice`


    Returns
    -------
    Device: `Schema Device`
        Device created in database

    """
    try:
        return await device_service.create(
            obj_in=DeviceCreate(**new_device.dict(), user_id=current_user.id)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=DeviceInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.DEVICE_FOUND_MSG},
        404: {"description": constants.DEVICE_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DeviceInDB:
    """
    Get Device by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Device: `Schema Device`
        Return an Device from the Database.
    """
    try:
        device = await device_service.get_by_id(_id=id)
        if not device["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return device
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.DEVICE_UPDATED_MSG},
        404: {"description": constants.DEVICE_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def update(
    update_device: DeviceUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Device.

    Update an Device in the database

    Parameters
    ----------
    id: `int`
    update_device: Schema `UpdateDevice`

    """
    try:
        device = await device_service.get_by_id(_id=id)
        if not device["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        device = await device_service.update(_id=id, obj_in=update_device)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.DEVICE_DELETED_MSG},
        404: {"description": constants.DEVICE_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Device.

    Delete an Device in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        device = await device_service.get_by_id(_id=id)
        if not device["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        device = await device_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/log-out/{token}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.DEVICE_UPDATED_MSG},
        404: {"description": constants.DEVICE_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def log_out(token: str = Path(...)) -> None:
    """
    Delete Device.

    Delete an Device in the database

    Parameters
    ----------
    id: `int`


    """
    device = await device_service.log_out(token=token)
    return None
