from typing import Union

from fastapi import APIRouter, status, Path, HTTPException, Depends, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.plan import (
    PlanInDB,
    PlanCreate,
    PlanUpdate,
    SearchPlan,
    PlanBase,
    PlanDetailed,
    PlanFullCreate,
    PlanFollow,
    GetAllReturn,
)
from app.schemas.results import (
    ResultsInDB,
    ResultOutput,
    StocksResponse,
)
from app.schemas import income, expenditure, saving, target, loan
from app.schemas.plandetail import PlanDetailCreate, PlanDetailDTO
from app.schemas.plan import ResultQuery
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.plan import plan_service
from app.services.results import results_service
from app.helpers.errors import ServiceException


router = APIRouter()


@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.PLAN_FOUND_MSG}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_all(
    skip: int = 0,
    limit: int = 10,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> GetAllReturn:
    """
    Get All Plans.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchPlan`

    Returns
    -------
    List: `Plan`
        List All Plans from the database.
    """
    try:
        return await plan_service.get_all(
            skip=skip,
            limit=limit,
            payload=SearchPlan(user_id=current_user.id).dict(),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=PlanInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.PLAN_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create(
    new_plan: PlanBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> PlanInDB:
    """
    Create Plan.


    Create an Plan in the database.

    Parameters
    ----------
    new_plan: Schema `CreatePlan`


    Returns
    -------
    Plan: `Schema Plan`
        Plan created in database

    """
    try:
        return await plan_service.create(
            obj_in=PlanCreate(**new_plan.dict(), user_id=current_user.id)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "/full-create",
    response_class=JSONResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.PLAN_CREATED_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def full_create(
    incomes: list[income.IncomeBase],
    expenditures: list[expenditure.ExpenditureBase],
    savings: list[saving.SavingBase],
    targets: list[target.TargetBase],
    loans: list[loan.LoanBase],
    new_plan: PlanBase = PlanBase(),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
):
    try:
        plan_full_create = PlanFullCreate(
            user_id=current_user.id,
            incomes=incomes,
            expenditures=expenditures,
            savings=savings,
            targets=targets,
            loans=loans,
            **new_plan.dict(),
        )
        return await plan_service.full_create(obj_in=plan_full_create)
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "/details",
    response_class=JSONResponse,
    status_code=status.HTTP_201_CREATED,
    response_model=PlanDetailed,
    responses={
        201: {"description": constants.PLAN_DETAIL_CREATED_MSG},
        404: {"description": constants.PLAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def create_details(
    plan_details: PlanDetailCreate,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> PlanDetailed:
    """
    Create Plan details.


    Create an PlanDetail in the database.

    Parameters
    ----------
    new_plan: Schema `PlanDetailCreate`


    Returns
    -------
    Plan: `Schema Plan Detailed`
        Plan created in database

    """
    try:
        plan = await plan_service.create_details(
            obj_in=PlanDetailDTO(
                **plan_details.dict(), user_id=current_user.id
            )
        )
        return plan
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}/detailed",
    response_class=JSONResponse,
    status_code=status.HTTP_200_OK,
    response_model=PlanDetailed,
    responses={
        200: {"description": constants.PLAN_FOUND_MSG},
        404: {"description": constants.PLAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_detailed(
    id: int, current_user: LoggedUser = Depends(deps.get_current_active_user)
):
    """
    Get Plan Detailed by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Plan: `Schema Plan Detailed`
        Return an Plan from the Database.
    """
    try:
        plan = await plan_service.get_detailed(id=id)
        if not plan["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return plan
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=PlanInDB,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.PLAN_FOUND_MSG},
        404: {"description": constants.PLAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def by_id(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> PlanInDB:
    """
    Get Plan by Id.

    Parameters
    ----------
    id: `int`

    Returns
    -------
    Plan: `Schema Plan`
        Return an Plan from the Database.
    """
    try:
        plan = await plan_service.get_by_id(_id=id)
        if not plan["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        return plan
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get("/{id}/results")
async def plan_results(
    id: int,
    payload: ResultQuery = Depends(),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> Union[ResultOutput, ResultsInDB]:
    try:
        return await results_service.get_by_id(
            _id=id,
            route="/plan",
            params=payload.dict(exclude_unset=True, exclude_none=True),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get("/{id}/stocks")
async def plan_loans_mortgages_by_year(
    id: int,
    year: str = Query(),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> StocksResponse:
    try:
        return await results_service.get_stocks_by(year=year, id=id)
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/follow/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.PLAN_UPDATED_MSG},
        404: {"description": constants.PLAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def follow_plan(
    id: int, current_user: LoggedUser = Depends(deps.get_current_active_user)
) -> None:
    try:
        print("Entra quí")
        plan = await plan_service.follow_plan(
            id=id, obj_in=PlanFollow(user_id=current_user.id)
        )
        if plan is False:
            raise HTTPException(
                status_code=404, detail=constants.PLAN_NOT_FOUND_MSG
            )
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.PLAN_UPDATED_MSG},
        404: {"description": constants.PLAN_NOT_FOUND_MSG},
    },
)
async def update(
    update_plan: PlanUpdate,
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update Plan.

    Update an Plan in the database

    Parameters
    ----------
    id: `int`
    update_plan: Schema `UpdatePlan`

    """
    try:
        plan = await plan_service.get_by_id(_id=id)
        if not plan["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        plan = await plan_service.update(_id=id, obj_in=update_plan)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": constants.PLAN_DELETED_MSG},
        404: {"description": constants.PLAN_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def delete(
    id: int = Path(..., gt=0),
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete Plan.

    Delete an Plan in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        plan = await plan_service.get_by_id(_id=id)
        if not plan["user_id"] == current_user.id:
            raise (
                HTTPException(
                    status.HTTP_403_FORBIDDEN,
                    constants.INVALID_CREDENTIALS_MSG,
                )
            )
        plan = await plan_service.delete(_id=id)
        if plan.status_code == 204:
            results = await results_service.delete(_id=id, route="/plan")
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
