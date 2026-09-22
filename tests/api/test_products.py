import requests
import pytest

def test_get_products(base_url):
    response=requests.get(f"{base_url}/api/products")
    data=response.json()
    print(data)
    #print(response.status_code)
    #print(response.headers)
    #print(response.text)
    assert response.status_code==200
    assert len(data)>0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "price" in data[0]
    assert isinstance(data[0]["price"],(float,int))
    for product in data:
        assert "id" in product
        print(f"{product['name']}: van ID")
        assert "name" in product
        print(f"{product['name']}: van NÉV")
        assert "price" in product
        print(f"{product['name']}: van PRICE")
        assert product["price"]>0
        print(f"{product['name']}: PRICE>0")

def test_negative(base_url):
    response=requests.get(f"{base_url}/api/products/999999")
    assert response.status_code == 404
    print(response.text)

def test_create_product_missing_data(base_url):
    response = requests.post(f"{base_url}/api/products", json={"name": "Csak ezt adom meg mas mezot nem"})
    assert response.status_code == 400
    print(response.status_code)

def test_create_product_wrong_price(base_url):
    response = requests.post(f"{base_url}/api/products", json={"name":"TestName", "price": "text not value"})
    assert response.status_code == 500
    print(response.status_code)

# def test_create_product(base_url):
#     response = requests.post(f"{base_url}/api/products",
#         json={
#             "name": "Test Product 4",
#             "price": 29.99
#         }
#     )
#     assert response.status_code == 201
#     data=response.json()
#     assert data["name"] == "Test Product 4"
#     print(response.text)

# def test_update_product(base_url):
#     response = requests.put(
#         f"{base_url}/api/products/18",
#         json={
#             "name": "Updated Product",
#             "price": 39.99
#         }
#     )
#     assert response.status_code == 200
#     print(response.text)

# def test_delete_product(base_url):
#     response = requests.delete(f"{base_url}/api/products/18"
#     )
#     assert response.status_code == 200
#     response = requests.get(f"{base_url}/api/products/18")
#     assert response.status_code == 404

def test_update_product(base_url, test_product):
    response = requests.put(
        f"{base_url}/api/products/{test_product}",
        json={
            "name": "Updated Product",
            "price": 39.99
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Product"
    assert data["price"] == 39.99