from fastapi.testclient import TestClient
from main import app

import pytest


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c