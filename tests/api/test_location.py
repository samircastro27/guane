import pytest
from fastapi.testclient import TestClient

from app.services.location import location_service
from tests.utils import constants as test_constants


@pytest.mark.asyncio
async def test_get_all_departments(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch
):
    async def mock_get_all(skip=0, limit=1, payload={}, route=""):
        return []

    monkeypatch.setattr(location_service, "get_all", mock_get_all)

    response = test_app.get(
        url=f"{test_constants.DEPARMENT_PREFIX}",
        params={"skip": 0, "limit": 1},
    )
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_get_cities_bydepartment(
    test_app: TestClient, monkeypatch: pytest.MonkeyPatch
):
    async def mock_get_all(skip=0, limit=1, payload={}, route=""):
        return []

    monkeypatch.setattr(location_service, "get_all", mock_get_all)

    response = test_app.get(
        url=f"{test_constants.DEPARMENT_PREFIX}/1/cities",
        params={"skip": 0, "limit": 1},
    )
    assert response.status_code == 200
    assert response.json() == []
