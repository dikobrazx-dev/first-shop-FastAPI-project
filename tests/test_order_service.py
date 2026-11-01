import asyncio
import pytest
from unittest.mock import AsyncMock
from services.order_service import OrderService
from exceptions import OrderNotFoundError, UserNotFoundError, ProductNotFoundError, InvalidQuantityError


@pytest.fixture
def mock_order_repo():
    return AsyncMock()


@pytest.fixture
def mock_user_service():
    return AsyncMock()


@pytest.fixture
def mock_product_service():
    return AsyncMock()


@pytest.fixture
def order_service(mock_order_repo, mock_user_service, mock_product_service):
    return OrderService(mock_order_repo, mock_user_service, mock_product_service)


def test_add_order_validates_user_exists(order_service, mock_order_repo, mock_user_service):
    """Перед созданием заказа сервис проверяет, что пользователь существует."""
    mock_user_service.get_user.return_value = AsyncMock()  # пользователь найден
    mock_order_repo.add_order.return_value = AsyncMock()

    asyncio.run(order_service.add_order(1))

    mock_user_service.get_user.assert_called_once_with(1)
    mock_order_repo.add_order.assert_called_once_with(1)


def test_add_order_raises_when_user_not_found(order_service, mock_user_service):
    """Если пользователя нет, выбрасывается UserNotFoundError."""
    mock_user_service.get_user.return_value = None

    with pytest.raises(UserNotFoundError):
        asyncio.run(order_service.add_order(999))


def test_get_order_raises_when_not_found(order_service, mock_order_repo):
    """Если заказа нет, выбрасывается OrderNotFoundError."""
    mock_order_repo.get_order.return_value = None

    with pytest.raises(OrderNotFoundError):
        asyncio.run(order_service.get_order(555))


def test_add_order_item_rejects_zero_quantity(order_service):
    """Количество 0 должно выбросить InvalidQuantityError."""
    with pytest.raises(InvalidQuantityError):
        asyncio.run(order_service.add_order_item(1, 1, 0))


def test_add_order_item_rejects_negative_quantity(order_service):
    """Отрицательное количество должно выбросить InvalidQuantityError."""
    with pytest.raises(InvalidQuantityError):
        asyncio.run(order_service.add_order_item(1, 1, -3))


def test_add_order_item_validates_order_and_product(order_service, mock_order_repo, mock_product_service):
    """Перед добавлением позиции проверяются заказ и товар."""
    mock_order_repo.get_order.return_value = AsyncMock()
    mock_product_service.get_product.return_value = AsyncMock()

    asyncio.run(order_service.add_order_item(1, 2, 5))

    mock_order_repo.get_order.assert_called_once_with(1)
    mock_product_service.get_product.assert_called_once_with(2)
    mock_order_repo.add_order_item.assert_called_once_with(1, 2, 5)


def test_total_price_calculates_sum(order_service, mock_order_repo):
    """Сервис должен правильно посчитать сумму заказа."""
    # Создаём фейковый заказ с позициями
    mock_item1 = AsyncMock()
    mock_item1.quantity = 2
    mock_item1.product.price = 10.0

    mock_item2 = AsyncMock()
    mock_item2.quantity = 3
    mock_item2.product.price = 5.0

    mock_order = AsyncMock()
    mock_order.items = [mock_item1, mock_item2]

    mock_order_repo.get_order_with_items.return_value = mock_order

    result = asyncio.run(order_service.total_price(1))

    assert result == 35.0  # 2*10 + 3*5
    mock_order_repo.get_order_with_items.assert_called_once_with(1)