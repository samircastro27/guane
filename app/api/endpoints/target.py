from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.target import (
    TargetInDB,
    TargetCreate,
    TargetUpdate,
    TargetBase,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.schemas.general import UserFilter
from app.core import constants, deps
from app.services.target import target_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.TARGET_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Targets.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchTarget`

    Returns
    -------
    List: `Target`
        List All Targets from the database.
    """
    try:
        return await target_service.get_all(
            skip=skip,
            limit=limit,
            payload=UserFilter(user_id=current_user.id).dict(),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=TargetInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.TARGET_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_target: TargetBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> TargetInDB:
    """
    Create Target.


    Create an Target in the database.

    Parameters
    ----------
    new_target: Schema `CreateTarget`


    Returns
    -------
    Target: `Schema Target`
        Target created in database

    """
    try:
        return await target_service.create(
            obj_in=TargetCreate(**new_target.dict(), user_id=current_user.id)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=TargetInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.TARGET_FOUND_MSG},
        404: {"description": constants.TARGET_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> TargetInDB:
    """
    Get Target by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Target: `Schema Target`
        Return an Target from the Database.
    """
    try:
        target = await target_service.get_by_id(_id=id)
        if not target["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return target
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.TARGET_UPDATED_MSG},
        404: {"description": constants.TARGET_NOT_FOUND_MSG},
    },
)
async def update(
    update_target: TargetUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Target.

    Update an Target in the database

    Parameters
    ----------
    id: `int`
    update_target: Schema `UpdateTarget`

    """
    try:
        target = await target_service.get_by_id(_id=id)
        if not target["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        target = await target_service.update(_id=id, obj_in=update_target)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.TARGET_DELETED_MSG},
        404: {"description": constants.TARGET_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Target.

    Delete an Target in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        target = await target_service.get_by_id(_id=id)
        if not target["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        target = await target_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
