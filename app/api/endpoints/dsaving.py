from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.dsaving import (
    DsavingInDB,
    DsavingBase,
    DsavingCreate,
    DsavingUpdate,
    DsavingMultiResponse,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.dsaving import dsaving_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.DSAVINGS_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Default savings.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchDsaving`

    Returns
    -------
    List: `Dsaving`
        List All Default savings from the database.
    """
    try:
        return await dsaving_service.get_all(
            skip=skip,
            limit=limit,
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=DsavingInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.DSAVING_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_dsaving: DsavingCreate,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DsavingInDB:
    """
    Create Default saving.


    Create an Default saving in the database.

    Parameters
    ----------
    new_dsaving: Schema `CreateDsaving`


    Returns
    -------
    Default saving: `Schema Default saving`
        Default saving created in database

    """
    try:
        return await dsaving_service.create(obj_in=new_dsaving)
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=DsavingInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.DSAVING_FOUND_MSG},
        404: {"description": constants.DSAVING_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DsavingInDB:
    """
    Get Default saving by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Default saving: `Schema Default saving`
        Return an Default saving from the Database.
    """
    try:
        dsaving = await dsaving_service.get_by_id(_id=id)
        return dsaving
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.DSAVING_UPDATED_MSG},
        404: {"description": constants.DSAVING_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def update(
    update_dsaving: DsavingUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Default saving.

    Update an Default saving in the database

    Parameters
    ----------
    id: `int`
    update_dsaving: Schema `UpdateDsaving`

    """
    try:
        dsaving = await dsaving_service.update(_id=id, obj_in=update_dsaving)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.DSAVING_DELETED_MSG},
        404: {"description": constants.DSAVING_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Default saving.

    Delete an Default saving in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        dsaving = await dsaving_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
