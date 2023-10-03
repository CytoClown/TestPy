import requests
import pytest
from pprint import pprint

BASE_URL = 'https://www.advantageonlineshopping.com/'
TOKEN_URL = 'accountservice/accountrest/api/v1/login'
POST_URL = 'catalog/api/v1/products'


def test_get_product(product_id):
    response = requests.get(f'{BASE_URL}{POST_URL}/{product_id}')
    assert response.status_code == 200, f'Status code is not {response.status_code}'
    print(f'Status code: {response.status_code}')
    # pprint(response.json())

def test_upd_product(token, product_id):
    product_id -= 1
    HEADER = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {token}'
    }
    payload = {
        "attributes": [
            {
                "attributeName": "qw",
                "attributeValue": "Intel"
            }
        ],
        "categoryId": 1,
        "colors": [
            {
                "code": "C3C3C3",
                "inStock": 10,
                "name": "Gray"
            }
        ],
        "description": "string",
        "imageUrl": "1100",
        "images": [
            "DD3A5B##1101"
        ],
        "price": 350,
        "productId": product_id,
        "productName": "Notebook",
        "productStatus": "Active"
    }
    response = requests.put(f'{BASE_URL}{POST_URL}/{product_id}', headers=HEADER, json=payload)
    assert response.status_code == 200, f'Status code is not {response.status_code}'
    assert response.json()['id'] == product_id
    print(f'Status code: {response.status_code}')
    # pprint(response.json())

def test_delete(token, product_id):
    product_id -= 2
    HEADER = {
        'Accept': '*/*',
        'Authorization': f'Bearer {token}'
    }
    response = requests.delete(f'{BASE_URL}{POST_URL}/{product_id}', headers=HEADER)
    assert response.status_code == 200, f'Status code is not {response.status_code}'
    print(f'Status code: {response.status_code}')
    # pprint(response.json())


def test_get_deleted_product(product_id):
    product_id -= 3
    response = requests.get(f'{BASE_URL}{POST_URL}/{product_id}')
    assert response.status_code == 404, f'Status code is not {response.status_code}'
    print(f'Status code: {response.status_code}')
