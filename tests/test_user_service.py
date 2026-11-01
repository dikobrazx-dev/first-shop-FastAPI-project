import asyncio
import pytest
from unittest.mock import AsyncMock
from services.user_service import UserService
from exceptions import UserNotFoundError


@pytest.fixture
def mock_repo():
    return AsyncMock()


@pytest.fixture
def user_service(mock_repo):
    return UserService(mock_repo)


def test_add_user_calls_repository_with_name(user_service, mock_repo):
    """Сервис должен передать имя в репозиторий."""
    asyncio.run(user_service.add_user("Alice"))
    mock_repo.add_user.assert_called_once_with("Alice")


def test_get_user_returns_repository_result(user_service, mock_repo):
    """Сервис должен вернуть то, что вернул репозиторий."""
    mock_user = AsyncMock()
    mock_user.id = 1
    mock_user.name = "Alice"
    mock_repo.get_user.return_value = mock_user

    result = asyncio.run(user_service.get_user(1))

    assert result is mock_user
    mock_repo.get_user.assert_called_once_with(1)


def test_get_user_raises_when_not_found(user_service, mock_repo):
    """Если репозиторий вернул None, сервис должен выбросить UserNotFoundError."""
    mock_repo.get_user.return_value = None

    with pytest.raises(UserNotFoundError):
        asyncio.run(user_service.get_user(999))


def test_get_users_returns_list(user_service, mock_repo):
    """Сервис должен вернуть список пользователей из репозитория."""
    mock_users = [AsyncMock(), AsyncMock()]
    mock_repo.get_users.return_value = mock_users

    result = asyncio.run(user_service.get_users())

    assert result == mock_users
    mock_repo.get_users.assert_called_once()


def test_update_user_calls_repository(user_service, mock_repo):
    """При обновлении имя передаётся в репозиторий вместе с id."""
    asyncio.run(user_service.update_user(1, "New Name"))
    mock_repo.update_user.assert_called_once_with(1, "New Name")


def test_delete_user_calls_repository(user_service, mock_repo):
    """При удалении в репозиторий передаётся id."""
    asyncio.run(user_service.delete_user(5))
    mock_repo.delete_user.assert_called_once_with(5)