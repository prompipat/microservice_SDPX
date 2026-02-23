from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_mul10():
    response = client.get("/mul10/5")
    assert response.status_code == 200
    assert response.json()["result"] == 50

def test_mul10_negative():
    response = client.get("/mul10/-5")
    assert response.status_code == 200
    assert response.json()["result"] == -50