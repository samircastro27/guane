import pytest
from fastapi.testclient import TestClient

from app.core import deps
from app.services.storage import storage_service
from app.main import app
from tests.utils import constants as test_constants
from tests.utils import data as test_data
from tests.utils.tools import user_fake


# Post full plan
def test_post_storage(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_or_create(obj_in):
        return test_data.storage, 201
    
    async def mock_create_or_update(obj_in):
        return test_data.storage, 200

    monkeypatch.setattr(
        storage_service, "get_or_create", mock_get_or_create
    )
    monkeypatch.setattr(
        storage_service, "create_or_update", mock_create_or_update
    )

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.STORAGE_PREFIX}/get-or-create",
            json=test_data.storage,
        )
        response_update = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.STORAGE_PREFIX}/create-or-update",
            json=test_data.storage,
        )
        assert response.status_code == 201
        assert response_update.status_code == 200
        return None
