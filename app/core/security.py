from fastapi.security import APIKeyHeader
from fastapi import Security, Depends, HTTPException, status

api_keys = ["guane123"]  # This is encrypted in the database

api_key_header = APIKeyHeader(
    name="access-token", auto_error=False
)  # use token authentication, important to use Depends
# The header must be: access-token: guane123


def api_key_auth(api_key: str = Security(api_key_header)):
    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate API KEY",
        )
    return api_key
