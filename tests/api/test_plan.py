import pytest
from fastapi.testclient import TestClient

from app.core import deps
from app.services.plan import plan_service
from app.services.results import results_service
from app.main import app
from tests.utils import constants as test_constants
from tests.utils import data as test_data
from tests.utils.tools import user_fake


class Response:
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code


# Get all
def test_get_all(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_all(skip, limit, payload):
        return [test_data.plan_response]

    monkeypatch.setattr(plan_service, "get_all", mock_get_all)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}"
        )
        assert response.status_code == 200
        return None


# Post an plan
def test_post(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_create(obj_in):
        return test_data.plan_response

    monkeypatch.setattr(plan_service, "create", mock_create)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}",
            json=test_data.plan_post,
        )
        assert response.status_code == 201
        return None


# Post empty file test
def test_post_empty(test_app: TestClient, fastapi_dep) -> None:
    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}"
        )
        assert response.status_code == 422
        return None


# Get by id
def test_get_by_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_by_id(_id: int):
        return test_data.plan_response

    monkeypatch.setattr(plan_service, "get_by_id", mock_get_by_id)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1"
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

    monkeypatch.setattr(plan_service, "update", mock_update)
    monkeypatch.setattr(plan_service, "get_by_id", mock_get_by_id)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.patch(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1",
            json=test_data.plan_update,
        )
        assert response.status_code == 204
        return None


# Patch None
def test_patch_by_id_fail(test_app: TestClient, fastapi_dep) -> None:
    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.patch(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1"
        )
        assert response.status_code == 422
        return None


# # Delete test
def test_delete_by_id(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_delete(_id, route=None):
        return Response(status_code=204)

    async def mock_get_by_id(_id):
        user = await user_fake()
        return {"user_id": user.id}

    monkeypatch.setattr(plan_service, "delete", mock_delete)
    monkeypatch.setattr(plan_service, "get_by_id", mock_get_by_id)
    monkeypatch.setattr(results_service, "delete", mock_delete)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.delete(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1"
        )
        assert response.status_code == 204
        return None


# Post details
def test_post_details(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_create_details(obj_in):
        return test_data.plan_detailed

    async def mock_get_detailed(id):
        return test_data.plan_detailed

    async def mock_get_by_id(_id):
        user = await user_fake()
        return {"user_id": user.id}

    monkeypatch.setattr(plan_service, "get_by_id", mock_get_by_id)
    monkeypatch.setattr(plan_service, "create_details", mock_create_details)
    monkeypatch.setattr(plan_service, "get_detailed", mock_get_detailed)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/details",
            json=test_data.plan_details,
        )
        assert response.status_code == 201
        return None


# Get detailed
def test_get_detailed(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_detailed(id):
        return test_data.plan_detailed

    async def mock_get_by_id(_id):
        user = await user_fake()
        return {"user_id": user.id}

    monkeypatch.setattr(plan_service, "get_by_id", mock_get_by_id)
    monkeypatch.setattr(plan_service, "get_detailed", mock_get_detailed)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1/detailed"
        )
        assert response.status_code == 200
        return None


# Post full plan
def test_post_full_create(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_full_create(obj_in):
        return test_data.plan_detailed

    monkeypatch.setattr(plan_service, "full_create", mock_full_create)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.post(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/full-create",
            json=test_data.plan_full_create,
        )
        assert response.status_code == 201
        return None


# Plan Follow
def test_follow_plan(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_follow_plan(id, obj_in):
        return None

    monkeypatch.setattr(plan_service, "follow_plan", mock_follow_plan)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.patch(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1/follow"
        )
        assert response.status_code == 204
        return None


# Get Results
def test_get_results(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_by_id(_id, route="", params=None):
        return test_data.plan_results

    monkeypatch.setattr(results_service, "get_by_id", mock_get_by_id)

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1/results"
        )
        assert response.status_code == 200
        return None


# Get Loans and Mortgages
def test_get_stocks(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch, fastapi_dep
) -> None:
    async def mock_get_stocks_by(year="", id=""):
        return test_data.stocks

    monkeypatch.setattr(
        results_service,
        "get_stocks_by",
        mock_get_stocks_by,
    )

    with fastapi_dep(app).override({deps.get_current_active_user: user_fake}):
        response = test_app.get(
            f"{test_constants.SERVICE_URL}{test_constants.PLAN_PREFIX}/1/stocks?year=2025"
        )
        assert response.status_code == 200
        return None
