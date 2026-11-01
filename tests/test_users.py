def test_create_user(client):
    """Создание пользователя: ожидаем 200 и сообщение об успехе."""
    response = client.post("/users/", json={"user_name": "Alice"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"] == "User has been successfully added"


def test_get_user_not_found(client):
    """Запрос несуществующего пользователя: ожидаем 404."""
    response = client.get("/users/999")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data


def test_get_users_list(client):
    """Получение списка пользователей: ожидаем 200 и список."""
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_update_user(client):
    """Обновление имени пользователя: создаём, узнаём id, меняем имя."""
    client.post("/users/", json={"user_name": "Bob"})
    users = client.get("/users/").json()
    user_id = users[-1]["id"]  # берём последнего созданного

    response = client.put(f"/users/{user_id}", json={"user_name": "Bob Updated"})
    assert response.status_code == 200


def test_delete_user(client):
    """Удаление пользователя: создаём, узнаём id, удаляем."""
    client.post("/users/", json={"user_name": "ToDelete"})
    users = client.get("/users/").json()
    user_id = users[-1]["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200