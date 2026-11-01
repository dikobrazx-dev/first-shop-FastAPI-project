def test_create_order(client):
    """Создание заказа: сначала нужен пользователь, потом заказ."""
    client.post("/users/", json={"user_name": "Order User"})
    users = client.get("/users/").json()
    user_id = users[-1]["id"]

    response = client.post("/orders/", json={"user_id": user_id})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"


def test_get_order_not_found(client):
    """Запрос несуществующего заказа: ожидаем 404."""
    response = client.get("/orders/999")
    assert response.status_code == 404


def test_add_order_item(client):
    """Добавление товара в заказ: нужны пользователь, товар и заказ."""
    # Создаём пользователя
    client.post("/users/", json={"user_name": "Item User"})
    users = client.get("/users/").json()
    user_id = users[-1]["id"]

    # Создаём товар
    client.post("/products/", json={"product_name": "Item Product", "product_price": 10})
    products = client.get("/products/").json()
    product_id = products[-1]["id"]

    # Создаём заказ (предполагаем, что это первый заказ и его id = 1)
    client.post("/orders/", json={"user_id": user_id})

    response = client.post("/orders/items", json={
        "item_order_id": 1,
        "item_product_id": product_id,
        "item_quantity": 2
    })
    assert response.status_code == 200


def test_get_order_items(client):
    """Получение позиций заказа: ожидаем 200 и список."""
    response = client.get("/orders/1/items")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_delete_order_item(client):
    """Удаление позиции из заказа: ожидаем 200."""
    # Создаём пользователя и товар, если ещё нет
    client.post("/users/", json={"user_name": "Delete User"})
    users = client.get("/users/").json()
    user_id = users[-1]["id"]

    client.post("/products/", json={"product_name": "Delete Product", "product_price": 5})
    products = client.get("/products/").json()
    product_id = products[-1]["id"]

    client.post("/orders/", json={"user_id": user_id})
    client.post("/orders/items", json={
        "item_order_id": 1,
        "item_product_id": product_id,
        "item_quantity": 1
    })

    response = client.delete(f"/orders/1/{product_id}")
    assert response.status_code == 200


def test_total_price(client):
    """Получение общей суммы заказа: ожидаем 200 и число."""
    response = client.get("/orders/1/total_price")
    assert response.status_code == 200
    # Ответ — это просто число (сумма), не объект
    assert isinstance(response.json(), (int, float))