from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.schemas.department import DepartmentInDB, SearchDepartment
from app.schemas.city import CityInDB, SearchCity
from app.core import constants as MSG
from app.helpers.errors.service import ServiceException
from app.services.location import location_service


router = APIRouter()


@router.get(
    "/department",
    response_class=JSONResponse,
    response_model=list[DepartmentInDB],
    status_code=status.HTTP_200_OK,
    responses={200: {"description": MSG.DEPARTMENTS_FOUND_MSG}},
)
async def get_all(
    payload: SearchDepartment = Depends(SearchDepartment),
) -> list[DepartmentInDB]:
    try:
        return await location_service.get_all(
            payload=payload.dict(exclude_none=True), route="/department"
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.get(
    "/department/{id}/cities",
    response_class=JSONResponse,
    response_model=list[CityInDB],
    status_code=status.HTTP_200_OK,
    responses={200: {"description": MSG.CITIES_FOUND_MSG}},
)
async def get_all_cities(
    id: int, payload: SearchCity = Depends(SearchCity)
) -> list[DepartmentInDB]:
    try:
        return await location_service.get_all(
            payload=payload.dict(exclude_none=True),
            route=f"/department/{id}/cities",
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
