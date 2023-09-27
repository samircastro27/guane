from fastapi import APIRouter, status, Path, HTTPException, Depends
from fastapi.responses import JSONResponse, Response

from app.schemas.loan import (
    LoanInDB,
    LoanBase,
    LoanCreate,
    LoanUpdate,
    SearchLoan,
    GetAllReturn,
    LoanTypeExtended,
    OptionsReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.loan import loan_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.LOANS_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    type: LoanTypeExtended = None,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Loans.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchLoan`

    Returns
    -------
    List: `Loan`
        List All Loans from the database.
    """
    try:
        return await loan_service.get_all(
            skip=skip,
            limit=limit,
            payload=SearchLoan(user_id=current_user.id, type=type).dict(
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
        return await loan_service.options(
            skip=skip, limit=limit, payload={"user_id": current_user.id}
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=LoanInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.LOAN_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_loan: LoanBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> LoanInDB:
    """
    Create Loan.


    Create an Loan in the database.

    Parameters
    ----------
    new_loan: Schema `CreateLoan`


    Returns
    -------
    Loan: `Schema Loan`
        Loan created in database

    """
    try:
        return await loan_service.create(
            obj_in=LoanCreate(**new_loan.dict(), user_id=current_user.id)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=LoanInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.LOAN_FOUND_MSG},
        404: {"description": constants.LOAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> LoanInDB:
    """
    Get Loan by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Loan: `Schema Loan`
        Return an Loan from the Database.
    """
    try:
        loan = await loan_service.get_by_id(_id=id)
        if not loan["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return loan
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.LOAN_UPDATED_MSG},
        404: {"description": constants.LOAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def update(
    update_loan: LoanUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Loan.

    Update an Loan in the database

    Parameters
    ----------
    id: `int`
    update_loan: Schema `UpdateLoan`

    """
    try:
        loan = await loan_service.get_by_id(_id=id)
        if not loan["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        loan = await loan_service.update(_id=id, obj_in=update_loan)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.LOAN_DELETED_MSG},
        404: {"description": constants.LOAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Loan.

    Delete an Loan in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        loan = await loan_service.get_by_id(_id=id)
        if not loan["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        loan = await loan_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
