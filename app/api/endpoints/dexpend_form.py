from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.schemas.dexpend_form import (
    DExpendFormInDB,
    DExpendFormCreate,
    DExpendFormBase,
    DExpendFormResponse,
)
from app.schemas.token import LoggedUser
from app.services.dexpend_form import dexpend_form_service
from app.helpers.errors import ServiceException
from app.core import deps

router = APIRouter()


@router.post(
    "/get-or-create",
    response_class=JSONResponse,
    response_model=DExpendFormResponse,
    responses={
        200: {"description": "DExpendForm obtained"},
        201: {"description": "DExpendForm created"},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_or_create(
    new_dexpend_form: DExpendFormBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> DExpendFormResponse:
    try:
        new_dexpend_form = DExpendFormCreate(
            **new_dexpend_form.dict(exclude_unset=True),
            user_id=current_user.id
        )
        dexpend_form, code = await dexpend_form_service.get_or_create(
            obj_in=new_dexpend_form
        )
        return JSONResponse(
            status_code=code,
            content=jsonable_encoder(dexpend_form),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


# @router.post(
#     "/create-or-update",
#     response_class=JSONResponse,
#     response_model=DExpendFormInDB,
#     responses={
#         200: {"description": "DExpendForm obtained"},
#         201: {"description": "DExpendForm created"},
#     },
#     dependencies=[Depends(deps.get_current_active_user)],
# )
# async def get_or_create_or_update(
#     new_dexpend_form: DExpendFormBase,
#     current_user: LoggedUser = Depends(deps.get_current_active_user),
# ) -> DExpendFormInDB:
#     try:
#         new_dexpend_form = DExpendFormCreate(
#             **new_dexpend_form.dict(exclude_unset=True),
#             user_id=current_user.id
#         )
#         dexpend_form, code = await dexpend_form_service.create_or_update(
#             obj_in=new_dexpend_form
#         )
#         return JSONResponse(
#             status_code=code,
#             content=jsonable_encoder(dexpend_form),
#         )
#     except ServiceException as e:
#         raise HTTPException(e.status_code, e.detail)
