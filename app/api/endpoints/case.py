from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.schemas.case import CaseInDB, CaseCreate, CaseBase
from app.schemas.token import LoggedUser
from app.services.case import case_service
from app.helpers.errors import ServiceException
from app.core import deps

router = APIRouter()


@router.get(
    "",
    response_model=CaseInDB,
    responses={200: {"description": "Case obtained"}},
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get(
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> CaseInDB:
    try:
        (case, code) = await case_service.get_or_create(
            obj_in=CaseCreate(user_id=current_user.id)
        )
        return case
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "/get-or-create",
    response_class=JSONResponse,
    response_model=CaseInDB,
    responses={
        200: {"description": "Case obtained"},
        201: {"description": "Case created"},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_or_create(
    new_case: CaseBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> CaseInDB:
    try:
        new_case = CaseCreate(**new_case.dict(exclude_unset=True), user_id=current_user.id)
        case, code = await case_service.get_or_create(obj_in=new_case)
        return JSONResponse(
            status_code=code,
            content=jsonable_encoder(case),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "/create-or-update",
    response_class=JSONResponse,
    response_model=CaseInDB,
    responses={
        200: {"description": "Case obtained"},
        201: {"description": "Case created"},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_or_create_or_update(
    new_case: CaseBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> CaseInDB:
    try:
        new_case = CaseCreate(**new_case.dict(exclude_unset=True), user_id=current_user.id)
        case, code = await case_service.create_or_update(obj_in=new_case)
        return JSONResponse(
            status_code=code,
            content=jsonable_encoder(case),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
