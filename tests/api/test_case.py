import pytest
from fastapi.testclient import TestClient

from app.core import deps
from app.services.case import case_service
from app.main import app
from tests.utils import constants as test_constants
from tests.utils import data as test_data
from tests.utils.tools import user_fake


# Update case
def test_update_case(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_create_or_update(obj_in):
        return test_data.case_response, 200

    async def mock_get_or_create(obj_in):
        return test_data.case_response, 201

    monkeypatch.setattr(
        case_service, "create_or_update", mock_create_or_update
    )
    monkeypatch.setattr(case_service, "get_or_create", mock_get_or_create)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        url = f"{test_constants.SERVICE_URL}{test_constants.CASE_PREFIX}"
        response_get = test_app.get(url)
        response_update = test_app.post(url+"/create-or-update", json=test_data.case_update)
        assert response_get.status_code == 200
        assert response_update.status_code == 200
        return None
