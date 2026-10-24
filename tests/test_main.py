from fastapi.testclient import TestClient

from src.main import app, base_de_dados

client = TestClient(app)


def setup_function():
    base_de_dados.clear()


def test_create_user_never_exposes_password():
    response = client.post(
        "/usuario", json={"id": 7, "email": "aluno@example.com", "senha": "demo-senha-forte"}
    )
    assert response.status_code == 201
    assert response.json() == {"id": 7, "email": "aluno@example.com"}
    assert "senha" not in str(client.get("/usuarios").json())
    assert "hash" not in str(client.get("/usuarios").json())


def test_duplicate_user_returns_conflict():
    data = {"id": 1, "email": "aluno@example.com", "senha": "demo-senha-forte"}
    assert client.post("/usuario", json=data).status_code == 201
    assert client.post("/usuario", json=data).status_code == 409


def test_missing_user_returns_404():
    assert client.get("/usuarios/404").status_code == 404


def test_short_password_rejected():
    result = client.post("/usuario", json={"id": 3, "email": "a@b.com", "senha": "123"})
    assert result.status_code == 422
