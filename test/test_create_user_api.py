from fastapi.testclient import TestClient
from src.delivery.fastapi_app import app

def test_create_user_endpoint_returns_created():
    client = TestClient(app)
    resp = client.post("/users", json={"first_name":"X","last_name":"Y"})
    assert resp.status_code == 200
    assert resp.json().get("status") == "created"
