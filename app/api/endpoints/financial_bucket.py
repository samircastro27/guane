from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.responses import JSONResponse
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.schemas.financial_bucket import (
    FinancialBucketCreate,
    FinancialBucketInDB,
)
from app.services.financial_bucket import financial_bucket_service

router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=FinancialBucketInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.FinancialBucket_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_FinancialBucket: FinancialBucketCreate,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> FinancialBucketInDB:
    """
    Create FinancialBucket.


    Create an FinancialBucket in the database.

    Parameters
    ----------
    new_FinancialBucket: Schema `CreateFinancialBucket`


    Returns
    -------
    FinancialBucket: `Schema FinancialBucket`
        FinancialBucket created in database

    """
    new_FinancialBucket.user_id = current_user.id
    return await financial_bucket_service.create(obj_in=new_FinancialBucket)


@router.get(
    "",
    response_class=JSONResponse,
    response_model=FinancialBucketInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.FinancialBucket_FOUND_MSG},
        404: {"description": constants.FinancialBucket_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> FinancialBucketInDB:
    """
    Get FinancialBucket by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    FinancialBucket: `Schema FinancialBucket`
        Return an FinancialBucket from the Database.
    """
    FinancialBucket = await financial_bucket_service.get_by_id(
        _id=current_user.id
    )
    if not FinancialBucket:
        raise HTTPException(
            status_code=404, detail=constants.FinancialBucket_NOT_FOUND_MSG
        )
    return FinancialBucket


@router.post(
    "/delete/item",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.FinancialBucket_DELETED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    new_FinancialBucket: FinancialBucketCreate,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
):
    """
    Delete FinancialBucket.


    Deletes an FinancialBucket item in the database.

    Parameters
    ----------
    new_FinancialBucket: Schema `CreateFinancialBucket`

    """
    new_FinancialBucket.user_id = current_user.id
    return await financial_bucket_service.delete_item(
        obj_in=new_FinancialBucket
    )
