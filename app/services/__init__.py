from .auth import AuthService
from app.infra.firebase.auth import AuthFireBase
from .user import user_service


auth_service = AuthService(auth=AuthFireBase)