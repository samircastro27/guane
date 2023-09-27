from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.token import Token
from app.services import auth_service
from app.helpers.errors import ServiceException

router = APIRouter()


@router.post(
    "/login/access-token",
    response_model=Token,
    status_code=200,
    responses={
        200: {"description": "Access Token"},
        400: {"description": "Inactive user"},
        401: {"description": "Incorrect username or password"},
    },
)
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Log in to the application.
    **Args**:
    - **form_data** (OAuth2PasswordRequestForm, optional): Standard OAuth2 scheme.
    **Raises**:
    - **401 HTTPException**: Incorrect username or password
    - **403 HTTPException**: Inactive user or blocked user
    **Returns**:
    - **Token**: Pydantic Model with the access token and the token type.
    """
    try:
        auth_response = await auth_service.authenticate(
            username=form_data.username, password=form_data.password
        )
        return Token(access_token=auth_response['idToken'], token_type="bearer")
    except ServiceException as e:
        raise HTTPException(e.status_code, e.detail)