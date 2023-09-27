from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.debt import (
    DebtInDB,
    DebtCreate,
    DebtUpdate,
    DebtMultiResponse,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.debt import debt_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.DEBTS_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Default debts.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchDebt`

    Returns
    -------
    List: `Debt`
        List All Default debts from the database.
    """
    try:
        return await debt_service.get_all(
            skip=skip,
            limit=limit,
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=DebtInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.DEBT_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_debt: DebtCreate,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DebtInDB:
    """
    Create Default debt.


    Create an Default debt in the database.

    Parameters
    ----------
    new_debt: Schema `CreateDebt`


    Returns
    -------
    Default debt: `Schema Default debt`
        Default debt created in database

    """
    try:
        return await debt_service.create(obj_in=new_debt)
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=DebtInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.DEBT_FOUND_MSG},
        404: {"description": constants.DEBT_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DebtInDB:
    """
    Get Default debt by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Default debt: `Schema Default debt`
        Return an Default debt from the Database.
    """
    try:
        debt = await debt_service.get_by_id(_id=id)
        return debt
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.DEBT_UPDATED_MSG},
        404: {"description": constants.DEBT_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def update(
    update_debt: DebtUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Default debt.

    Update an Default debt in the database

    Parameters
    ----------
    id: `int`
    update_debt: Schema `UpdateDebt`

    """
    try:
        debt = await debt_service.update(_id=id, obj_in=update_debt)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.DEBT_DELETED_MSG},
        404: {"description": constants.DEBT_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Default debt.

    Delete an Default debt in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        debt = await debt_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
