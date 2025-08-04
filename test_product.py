from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product_success():
    response = client.post("/products", json={"name": "Produto X", "price": 7000})
    assert response.status_code == 200
    assert "id" in response.json()

def test_create_product_failure():
    response = client.post("/products", json={"price": 7000})
    assert response.status_code == 500

def test_update_product_not_found():
    response = client.patch("/products/999", json={"name": "Novo Nome"})
    assert response.status_code == 404

def test_update_product_updated_at_auto():
    response = client.post("/products", json={"name": "Produto Y", "price": 6000})
    product_id = response.json()["id"]
    update_response = client.patch(f"/products/{product_id}", json={"price": 6100})
    assert update_response.status_code == 200
    assert "updated_at" in update_response.json()