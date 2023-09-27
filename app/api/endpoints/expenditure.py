from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.expenditure import (
    ExpenditureInDB,
    ExpenditureCreate,
    ExpenditureUpdate,
    SearchExpenditure,
    ExpenditureBase,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.expenditure import expenditure_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.EXPENDITURE_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Expenditures.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchExpenditure`

    Returns
    -------
    List: `Expenditure`
        List All Expenditures from the database.
    """
    try:
        return await expenditure_service.get_all(
            skip=skip,
            limit=limit,
            payload=SearchExpenditure(user_id=current_user.id).dict(),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=ExpenditureInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.EXPENDITURE_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_expenditure: ExpenditureBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> ExpenditureInDB:
    """
    Create Expenditure.


    Create an Expenditure in the database.

    Parameters
    ----------
    new_expenditure: Schema `CreateExpenditure`


    Returns
    -------
    Expenditure: `Schema Expenditure`
        Expenditure created in database

    """
    try:
        return await expenditure_service.create(
            obj_in=ExpenditureCreate(
                **new_expenditure.dict(), user_id=current_user.id
            )
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=ExpenditureInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.EXPENDITURE_FOUND_MSG},
        404: {"description": constants.EXPENDITURE_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> ExpenditureInDB:
    """
    Get Expenditure by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Expenditure: `Schema Expenditure`
        Return an Expenditure from the Database.
    """
    try:
        expenditure = await expenditure_service.get_by_id(_id=id)
        if not expenditure["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return expenditure
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.EXPENDITURE_UPDATED_MSG},
        404: {"description": constants.EXPENDITURE_NOT_FOUND_MSG},
    },
)
async def update(
    update_expenditure: ExpenditureUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Expenditure.

    Update an Expenditure in the database

    Parameters
    ----------
    id: `int`
    update_expenditure: Schema `UpdateExpenditure`

    """
    try:
        expenditure = await expenditure_service.get_by_id(_id=id)
        if not expenditure["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        expenditure = await expenditure_service.update(
            _id=id, obj_in=update_expenditure
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
        204: {"description": constants.EXPENDITURE_DELETED_MSG},
        404: {"description": constants.EXPENDITURE_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Expenditure.

    Delete an Expenditure in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        expenditure = await expenditure_service.get_by_id(_id=id)
        if not expenditure["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        expenditure = await expenditure_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
