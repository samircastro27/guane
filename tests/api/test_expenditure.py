import pytest
from fastapi.testclient import TestClient

from app.services.expenditure import expenditure_service
from app.core import deps
from app.main import app
from tests.utils import constants as test_constants
from tests.utils import data as test_data
from tests.utils.tools import user_fake


# Get all
def test_get_all(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_all(skip, limit, payload):
        return [test_data.expenditure_response]

    monkeypatch.setattr(expenditure_service, "get_all", mock_get_all)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.EXPENDITURE_PREFIX}"
        )
        assert response.status_code == 200
        return None


# Post an expenditure
def test_post(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_create(obj_in):
        return test_data.expenditure_response

    monkeypatch.setattr(expenditure_service, "create", mock_create)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.EXPENDITURE_PREFIX}",
            json=test_data.expenditure_post,
        )
        assert response.status_code == 201
        return None


# Post empty file test
def test_post_empty(test_app: TestClient, fastapi_dep) -> None:
    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.EXPENDITURE_PREFIX}"
        )
        assert response.status_code == 422
        return None


# Get by id
def test_get_by_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_by_id(_id: int):
        return test_data.expenditure_response

    monkeypatch.setattr(expenditure_service, "get_by_id", mock_get_by_id)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.EXPENDITURE_PREFIX}/1"
        )
        assert response.status_code == 200
        return None


# Patch by i
def test_patch_by_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_update(_id, obj_in):
        """mock update"""
        return None

    async def mock_get_by_id(_id):
        user = await user_fake()
        return {"user_id": user.id}

    monkeypatch.setattr(expenditure_service, "update", mock_update)
    monkeypatch.setattr(expenditure_service, "get_by_id", mock_get_by_id)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.patch(
            f"{test_constants.SERVICE_URL}{test_constants.EXPENDITURE_PREFIX}/1",
            json=test_data.expenditure_update,
        )
        assert response.status_code == 204
        return None


# Patch None
def test_patch_by_id_fail(test_app: TestClient, fastapi_dep) -> None:
    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.patch(
            f"{test_constants.SERVICE_URL}{test_constants.EXPENDITURE_PREFIX}/1"
        )
        assert response.status_code == 422
        return None


# # Delete test
def test_delete_by_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_delete(_id):
        """mock delete"""

    async def mock_get_by_id(_id):
        user = await user_fake()
        return {"user_id": user.id}

    monkeypatch.setattr(expenditure_service, "delete", mock_delete)
    monkeypatch.setattr(expenditure_service, "get_by_id", mock_get_by_id)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.delete(
            f"{test_constants.SERVICE_URL}{test_constants.EXPENDITURE_PREFIX}/1"
        )
        assert response.status_code == 204
        return None
