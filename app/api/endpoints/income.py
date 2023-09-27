from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.income import (
    IncomeInDB,
    IncomeBase,
    IncomeCreate,
    IncomeUpdate,
    SearchIncome,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.income import income_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.USERS_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Incomes.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchIncome`

    Returns
    -------
    List: `Income`
        List All Incomes from the database.
    """
    try:
        return await income_service.get_all(
            skip=skip,
            limit=limit,
            payload=SearchIncome(user_id=current_user.id).dict(),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=IncomeInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.USER_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_income: IncomeBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> IncomeInDB:
    """
    Create Income.


    Create an Income in the database.

    Parameters
    ----------
    new_income: Schema `CreateIncome`


    Returns
    -------
    Income: `Schema Income`
        Income created in database

    """
    try:
        return await income_service.create(
            obj_in=IncomeCreate(**new_income.dict(), user_id=current_user.id)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=IncomeInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.USER_FOUND_MSG},
        404: {"description": constants.USER_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> IncomeInDB:
    """
    Get Income by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Income: `Schema Income`
        Return an Income from the Database.
    """
    try:
        income = await income_service.get_by_id(_id=id)
        if not income["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return income
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.USER_UPDATED_MSG},
        404: {"description": constants.USER_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def update(
    update_income: IncomeUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Income.

    Update an Income in the database

    Parameters
    ----------
    id: `int`
    update_income: Schema `UpdateIncome`

    """
    try:
        income = await income_service.get_by_id(_id=id)
        if not income["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        income = await income_service.update(_id=id, obj_in=update_income)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.USER_DELETED_MSG},
        404: {"description": constants.USER_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Income.

    Delete an Income in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        income = await income_service.get_by_id(_id=id)
        if not income["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        income = await income_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
