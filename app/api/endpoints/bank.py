from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.bank import (
    BankInDB,
    BankBase,
    BankCreate,
    BankUpdate,
    BankMultiResponse,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.bank import bank_service
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
    Get All banks.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchBank`

    Returns
    -------
    List: `Bank`
        List All banks from the database.
    """
    try:
        return await bank_service.get_all(
            skip=skip,
            limit=limit,
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=BankInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.DEBT_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_bank: BankBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> BankInDB:
    """
       Create bank.


       Create an bank in the database.

       Parameters
       ----------
       new_bank: Schema `CreateBank`


       Returns
       -------
    bank: `Schema bank`
        bank created in database

    """
    try:
        return await bank_service.create(
            obj_in=BankCreate(**new_bank.dict(), user_id=current_user.id)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=BankInDB,
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
) -> BankInDB:
    """
       Get bank by Id.

       Parameters
       ----------
       id: `int`

       Returns
       -------
    bank: `Schema bank`
           Return an bank from the Database.
    """
    try:
        bank = await bank_service.get_by_id(_id=id)
        return bank
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
    update_bank: BankUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update bank.

    Update an bank in the database

    Parameters
    ----------
    id: `int`
    update_bank: Schema `UpdateBank`

    """
    try:
        bank = await bank_service.update(_id=id, obj_in=update_bank)
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
    Delete bank.

    Delete an bank in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        bank = await bank_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
