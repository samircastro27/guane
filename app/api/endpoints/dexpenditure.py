from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.dexpenditure import (
    DexpenditureInDB,
    DexpenditureCreate,
    DexpenditureUpdate,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.dexpenditure import dexpenditure_service
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
    Get All Default expenditures.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchDexpenditure`

    Returns
    -------
    List: `Dexpenditure`
        List All Default expenditures from the database.
    """
    try:
        return await dexpenditure_service.get_all(
            skip=skip,
            limit=limit,
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=DexpenditureInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.DSAVING_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_dexpenditure: DexpenditureCreate,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DexpenditureInDB:
    """
    Create Default expenditure.


    Create an Default expenditure in the database.

    Parameters
    ----------
    new_dexpenditure: Schema `CreateDexpenditure`


    Returns
    -------
    Default expenditure: `Schema Default expenditure`
        Default expenditure created in database

    """
    try:
        return await dexpenditure_service.create(obj_in=new_dexpenditure)
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=DexpenditureInDB,
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
) -> DexpenditureInDB:
    """
    Get Default expenditure by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Default expenditure: `Schema Default expenditure`
        Return an Default expenditure from the Database.
    """
    try:
        dexpenditure = await dexpenditure_service.get_by_id(_id=id)
        return dexpenditure
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
    update_dexpenditure: DexpenditureUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Default expenditure.

    Update an Default expenditure in the database

    Parameters
    ----------
    id: `int`
    update_dexpenditure: Schema `UpdateDexpenditure`

    """
    try:
        dexpenditure = await dexpenditure_service.update(
            _id=id, obj_in=update_dexpenditure
        )
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
    Delete Default expenditure.

    Delete an Default expenditure in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        dexpenditure = await dexpenditure_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
