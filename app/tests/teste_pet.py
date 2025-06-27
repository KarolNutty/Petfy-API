from fastapi.testclient import TestClient
from app.main import app
from app.core.database import create_db

create_db()  # cria as tabelas antes dos testes

client = TestClient(app)

def test_create_pet():
    payload = {
        "nome": "Tobby",
        "tipo": "Cachorro",
        "idade": 3,
        "adotado": False
    }

    response = client.post("/pets", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["nome"] == payload["nome"]
    assert data["tipo"] == payload["tipo"]
    assert data["idade"] == payload["idade"]
    assert data["adotado"] == payload["adotado"]
    assert "id" in data  # Garante que o ID foi gerado
