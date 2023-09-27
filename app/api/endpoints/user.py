from fastapi import APIRouter, status, Depends, Path, HTTPException
from fastapi.responses import JSONResponse, Response

from app.schemas.user import (
    UserInDB,
    UserSearch,
    UserCreate,
    UserUpdate,
    UserResponse,
    GetAllReturn,
)
from app.schemas.token import LoggedUser
from app.core import constants, deps
from app.services.user import user_service
from app.helpers.errors import ServiceException

router = APIRouter()


# Discuss how to handle admin endpoints
@router.get(
    "",
    response_class=JSONResponse,
    response_model=GetAllReturn,
    status_code=status.HTTP_200_OK,
    responses={200: {"description": constants.USERS_FOUND_MSG}},
)
async def get_all(
    skip: int = 0, limit: int = 10, payload: UserSearch = Depends(UserSearch)
) -> GetAllReturn:
    """
    Get All Users.

    Parameters
    ----------

    Skip: 0
    Limit: 10
    payload: Schema `SearchUser`

    Returns
    -------
    List: `User`
        List All Users from the database.
    """
    try:
        return await user_service.get_all(
            skip=skip, limit=limit, payload=payload.dict(exclude_none=True)
        )
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.post(
    "",
    response_class=JSONResponse,
    response_model=UserInDB,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": constants.USER_CREATED_MSG},
    },
)
async def create(new_user: UserCreate) -> UserInDB:
    """
    Create User.


    Create an User in the database.

    Parameters
    ----------
    new_user: Schema `CreateUser`


    Returns
    -------
    User: `Schema User`
        User created in database

    """
    try:
        return await user_service.create(obj_in=new_user)
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


# Discuss admin endpoints
# @router.get(
#     "/{id}",
#     response_class=JSONResponse,
#     response_model=UserResponse,
#     status_code=status.HTTP_200_OK,
#     responses={
#         200: {"description": constants.USER_FOUND_MSG},
#         404: {"description": constants.USER_NOT_FOUND_MSG},
#     },
#     dependencies=[Depends(deps.get_current_active_user)],
# )
# async def by_id(
#     id: int = Path(..., gt=0),
# ) -> UserResponse:
#     """
#     Get User by Id.

#     Parameters
#     ----------
#     id: `int`

#     Returns
#     -------
#     User: `Schema User`
#         Return an User from the Database.
#     """
#     try:
#         user = await user_service.get_by_id(_id=id)
#         return user
#     except ServiceException as e:
#         raise HTTPException(e.status_code, e.detail)


# Discuss admin endpoints
# @router.get(
#     "/uid/{uid}",
#     response_class=JSONResponse,
#     response_model=UserResponse,
#     status_code=status.HTTP_200_OK,
#     responses={
#         200: {"description": constants.USER_FOUND_MSG},
#         404: {"description": constants.USER_NOT_FOUND_MSG},
#     },
#     dependencies=[Depends(deps.get_current_active_user)],
# )
# async def get_by_uid(uid: str = Path(...)) -> UserResponse:
#     """
#     Get User by uid.

#     Parameters
#     ----------
#     id: `str` Query

#     Returns
#     -------
#     User: `Schema User`
#         Return an User from the Database.
#     """
#     try:
#         user = await user_service.get_by_uid(uid=uid)
#         return user
#     except ServiceException as e:
#         raise HTTPException(e.status_code, e.detail)


@router.get(
    "/current",
    response_class=JSONResponse,
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": constants.USER_FOUND_MSG},
        404: {"description": constants.USER_NOT_FOUND_MSG},
    },
    dependencies=[Depends(deps.get_current_active_user)],
)
async def get_by_uid(
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> UserResponse:
    """
    Get User by uid.

    Parameters
    ----------
    id: `str` Query

    Returns
    -------
    User: `Schema User`
        Return an User from the Database.
    """
    try:
        user = await user_service.get_by_uid(uid=current_user.uid)
        return user
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


@router.patch(
    "",
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
    update_user: UserUpdate,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Update User.

    Update an User in the database

    Parameters
    ----------
    id: `int`
    update_user: Schema `UpdateUser`

    """
    try:
        user = await user_service.update(
            _id=current_user.id, obj_in=update_user
        )
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)


# Discuss admin endpoints
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
    id: int,
    current_user: LoggedUser = Depends(deps.get_current_active_user),
) -> None:
    """
    Delete User.

    Delete an User in the database

    Parameters
    ----------
    id: `int`


    """
    try:
        user = await user_service.delete(_id=id)
        return None
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)
