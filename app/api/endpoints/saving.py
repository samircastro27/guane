from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.saving import (
    SavingInDB,
    SavingCreate,
    SavingUpdate,
    SearchSaving,
    SavingBase,
    GetAllReturn,
    Status,
    OptionsReturn
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.saving import saving_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.SAVING_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    status: Status = None,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Savings.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchSaving`

    Returns
    -------
    List: `Saving`
        List All Savings from the database.
    """
    try:
        return await saving_service.get_all(
            skip=skip,
            limit=limit,
            payload=SearchSaving(user_id=current_user.id, status=status).dict(
                exclude_none=True
            ),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/options",
    response_class=JSONResponse,
    response_model=OptionsReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.SAVING_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> OptionsReturn:
    """
    Get All Savings.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchSaving`

    Returns
    -------
    List: `Saving`
        List All Savings from the database.
    """
    try:
        return await saving_service.options(
            skip=skip, limit=limit, payload={"user_id": current_user.id}
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=SavingInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.SAVING_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_saving: SavingBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> SavingInDB:
    """
    Create Saving.


    Create an Saving in the database.

    Parameters
    ----------
    new_saving: Schema `CreateSaving`


    Returns
    -------
    Saving: `Schema Saving`
        Saving created in database

    """
    try:
        return await saving_service.create(
            obj_in=SavingCreate(**new_saving.dict(), user_id=current_user.id)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=SavingInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.SAVING_FOUND_MSG},
        404: {"description": constants.SAVING_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> SavingInDB:
    """
    Get Saving by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Saving: `Schema Saving`
        Return an Saving from the Database.
    """
    try:
        saving = await saving_service.get_by_id(_id=id)
        if not saving["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return saving
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.SAVING_UPDATED_MSG},
        404: {"description": constants.SAVING_NOT_FOUND_MSG},
    },
)
async def update(
    update_saving: SavingUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Saving.

    Update an Saving in the database

    Parameters
    ----------
    id: `int`
    update_saving: Schema `UpdateSaving`

    """
    try:
        saving = await saving_service.get_by_id(_id=id)
        if not saving["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        saving = await saving_service.update(_id=id, obj_in=update_saving)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.SAVING_DELETED_MSG},
        404: {"description": constants.SAVING_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Saving.

    Delete an Saving in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        saving = await saving_service.get_by_id(_id=id)
        if not saving["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        saving = await saving_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
