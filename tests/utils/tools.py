from app.schemas.token import LoggedUser
from app.schemas.general import Status


async def user_fake():
    return LoggedUser(
        id=1,
        uid="fakeuid",
        email="guane@example.com",
        email_verified=True,
        status=Status.ACTIVE,
    )


async def api_key_fake():
    return "fake_key"
