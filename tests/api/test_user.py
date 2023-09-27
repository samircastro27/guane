from typing import Any

import pytest
from fastapi.testclient import TestClient

from app.services.user import user_service
from app.main import app
from app.core import deps
from tests.utils import constants as test_constants
from tests.utils import data as test_data
from tests.utils.tools import user_fake



# Post an user
def test_post(test_app: TestClient, monkeypatch: pytest.MonkeyPatch) -> None:
    async def mock_create(obj_in):
        return test_data.user_response

    monkeypatch.setattr(user_service, "create", mock_create)

    response = test_app.post(
        f"{test_constants.SERVICE_URL}{test_constants.USER_PREFIX}",
        json=test_data.user_post,
    )
    assert response.status_code == 201
    return None


# Post empty file test
def test_post_empty(test_app: TestClient) -> None:
    response = test_app.post(
        f"{test_constants.SERVICE_URL}{test_constants.USER_PREFIX}"
    )
    assert response.status_code == 422
    return None


# Get by uid
def test_get_by_uid(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_by_uid(uid: str):
        return test_data.user_response

    monkeypatch.setattr(user_service, "get_by_uid", mock_get_by_uid)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.USER_PREFIX}/current"
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

    monkeypatch.setattr(user_service, "update", mock_update)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.patch(
            f"{test_constants.SERVICE_URL}{test_constants.USER_PREFIX}",
            json=test_data.user_1_update,
        )
        assert response.status_code == 204
        return None


# Patch None
def test_patch_by_id_fail(test_app: TestClient, fastapi_dep) -> None:
    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.patch(
            f"{test_constants.SERVICE_URL}{test_constants.USER_PREFIX}"
        )
        assert response.status_code == 422
        return None


# # Delete test
def test_delete_by_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_delete(_id):
        """mock delete"""

    monkeypatch.setattr(user_service, "delete", mock_delete)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.delete(
            f"{test_constants.SERVICE_URL}{test_constants.USER_PREFIX}"
        )
        assert response.status_code == 204
        return None
