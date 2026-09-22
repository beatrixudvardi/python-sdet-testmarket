import pytest
import requests

@pytest.fixture
def base_url():
    return "http://localhost:3000"

@pytest.fixture
def test_product(base_url):
    response = requests.post(
        f"{base_url}/api/products",
        json={
            "name": "Product For Test",
            "price": 10.00
        }
    )
    assert response.status_code == 201
    product_id = response.json()["id"]
    yield product_id

    requests.delete(
        f"{base_url}/api/products/{product_id}"
    )
