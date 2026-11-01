import asyncio
import pytest
from unittest.mock import AsyncMock
from services.product_service import ProductService
from exceptions import ProductNotFoundError


@pytest.fixture
def mock_repo():
    return AsyncMock()


@pytest.fixture
def product_service(mock_repo):
    return ProductService(mock_repo)


def test_add_product_calls_repository(product_service, mock_repo):
    """Сервис должен передать имя и цену в репозиторий."""
    asyncio.run(product_service.add_product("Apple", 100))
    mock_repo.add_product.assert_called_once_with("Apple", 100)


def test_get_product_returns_repository_result(product_service, mock_repo):
    """Сервис должен вернуть то, что вернул репозиторий."""
    mock_product = AsyncMock()
    mock_product.id = 1
    mock_product.name = "Apple"
    mock_product.price = 100.0
    mock_repo.get_product.return_value = mock_product

    result = asyncio.run(product_service.get_product(1))

    assert result is mock_product
    mock_repo.get_product.assert_called_with(1)


def test_get_product_raises_when_not_found(product_service, mock_repo):
    """Если репозиторий вернул None, сервис должен выбросить ProductNotFoundError."""
    mock_repo.get_product.return_value = None

    with pytest.raises(ProductNotFoundError):
        asyncio.run(product_service.get_product(999))


def test_get_products_returns_list(product_service, mock_repo):
    """Сервис должен вернуть список продуктов."""
    mock_products = [AsyncMock(), AsyncMock()]
    mock_repo.get_products.return_value = mock_products

    result = asyncio.run(product_service.get_products())

    assert result == mock_products
    mock_repo.get_products.assert_called_once()


def test_update_product_price_calls_repository(product_service, mock_repo):
    """При обновлении цены передаются id и новая цена."""
    asyncio.run(product_service.update_product_price(1, 150.0))
    mock_repo.update_product_price.assert_called_once_with(1, 150.0)


def test_delete_product_calls_repository(product_service, mock_repo):
    """При удалении в репозиторий передаётся id."""
    asyncio.run(product_service.delete_product(5))
    mock_repo.delete_product.assert_called_once_with(5)