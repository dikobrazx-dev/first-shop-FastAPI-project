def test_create_product(client):
    """Создание товара: ожидаем 200 и сообщение об успехе."""
    response = client.post("/products/", json={
        "product_name": "Apple",
        "product_price": 100
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"


def test_get_products_list(client):
    """Получение списка товаров: ожидаем 200 и список."""
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_update_product_price(client):
    """Обновление цены товара: создаём, узнаём id, меняем цену."""
    client.post("/products/", json={"product_name": "Bread", "product_price": 50})
    products = client.get("/products/").json()
    product_id = products[-1]["id"]

    response = client.put(f"/products/{product_id}", json={"new_price": 75})
    assert response.status_code == 200


def test_delete_product(client):
    """Удаление товара: создаём, узнаём id, удаляем."""
    client.post("/products/", json={"product_name": "Temp", "product_price": 10})
    products = client.get("/products/").json()
    product_id = products[-1]["id"]

    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200


def test_create_product_price_zero(client):
    """Цена товара 0: Pydantic должен вернуть 422."""
    response = client.post("/products/", json={
        "product_name": "Free",
        "product_price": 0
    })
    assert response.status_code == 422


def test_create_product_price_negative(client):
    """Отрицательная цена товара: Pydantic должен вернуть 422."""
    response = client.post("/products/", json={
        "product_name": "Debt",
        "product_price": -100
    })
    assert response.status_code == 422