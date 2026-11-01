import asyncio
from fastapi.testclient import TestClient
from main import app
from database.database import drop_tables, create_tables

import pytest


@pytest.fixture
def client():
    # Очищаем базу перед каждым тестом, чтобы тесты не зависели друг от друга
    asyncio.run(drop_tables())
    asyncio.run(create_tables())

    with TestClient(app) as c:
        yield c