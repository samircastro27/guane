import contextlib

import pytest
from fastapi.testclient import TestClient

from app.main import app
from tests.utils.overrider import FixtureDependencyOverrider


@pytest.fixture(scope="session")
def test_app():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def fastapi_dep(request):
    parametrized = getattr(request, "param", None)
    context = (
        FixtureDependencyOverrider(parametrized[0]).override(parametrized[1])
        if parametrized
        else contextlib.nullcontext()
    )

    with context:
        yield FixtureDependencyOverrider
