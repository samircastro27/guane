import pytest
from fastapi.testclient import TestClient

from app.services import auth_service
from tests.utils.data import token, decoded_token
from app.infra.firebase.auth import AuthFireBase

BASE_URL = "/api/v1/login/access-token"


@pytest.mark.asyncio
async def test_login_access_token(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch
):
    async def mock_authenticate(self, username="guane", password="guane"):
        return token

    async def mock_decode_token(self, token: str):
        return decoded_token

    monkeypatch.setattr(AuthFireBase, "decode_token", mock_decode_token)
    monkeypatch.setattr(AuthFireBase, "authenticate", mock_authenticate)
    
    fire_base_schema = await auth_service.decode_token("any token")

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = {"username": "testing", "password": "testing"}
    response = test_app.post(BASE_URL, data=body, headers=headers)

    assert response.json()["access_token"] == token["idToken"]
    assert fire_base_schema == decoded_token
