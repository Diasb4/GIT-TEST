import pytest
from Test import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200  # Проверяем, что ответ 200 (OK)
    data = response.get_json()
    assert len(data) == 2  # Проверяем, что список содержит 2 пользователя

def test_get_user_by_id(client):
    response = client.get('/user/1')
    assert response.status_code == 200  # Проверяем, что ответ 200
    data = response.get_json()
    assert data["name"] == "Алексей"  # Проверяем имя пользователя

def test_get_user_not_found(client):
    response = client.get('/user/999')
    assert response.status_code == 404  # Проверяем, что ошибка 404
    data = response.get_json()
    assert data["error"] == "User not found"  # Проверяем сообщение об ошибке