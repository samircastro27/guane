from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.schemas.storage import StorageInDB, StorageCreate, StorageBase
from app.schemas.token import LoggedUser
from app.services.storage import storage_service
from app.helpers.errors import ServiceException
from app.core import deps

router = APIRouter()


@router.post(
    "/get-or-create",
    response_class=JSONResponse,
    response_model=StorageInDB,
    responses={
        200: {"description": "Storage obtained"},
        201: {"description": "Storage created"},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_or_create(
    new_storage: StorageBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> StorageInDB:
    try:
        new_storage = StorageCreate(
            **new_storage.dict(), user_id=current_user.id
        )
        storage, code = await storage_service.get_or_create(
            obj_in=new_storage
        )
        return JSONResponse(
            status_code=code,
            content=jsonable_encoder(storage),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
    
    
@router.post(
    "/create-or-update",
    response_class=JSONResponse,
    response_model=StorageInDB,
    responses={
        200: {"description": "Storage obtained"},
        201: {"description": "Storage created"},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_or_create_or_update(
    new_storage: StorageBase,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> StorageInDB:
    try:
        new_storage = StorageCreate(
            **new_storage.dict(), user_id=current_user.id
        )
        storage, code = await storage_service.create_or_update(
            obj_in=new_storage
        )
        return JSONResponse(
            status_code=code,
            content=jsonable_encoder(storage),
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
