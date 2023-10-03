import pytest
import requests
from pprint import pprint

BASE_URL = 'https://www.advantageonlineshopping.com/'
TOKEN_URL = 'accountservice/accountrest/api/v1/login'
POST_URL = 'catalog/api/v1/products'


@pytest.fixture
def token():
    headers = {'Content-Type': 'application/json'}
    payload = {
      "email": "string@mail.ru",
      "loginPassword": "adm1n",
      "loginUser": "admin"
    }
    response = requests.post(f'{BASE_URL}{TOKEN_URL}', headers=headers, json=payload)
    token = response.json()['statusMessage']['token']
    assert response.status_code == 200, f'Status code is not {response.status_code}'
    yield token

@pytest.fixture
def product_id(token):
    HEADER = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Authorization': f'Bearer {token}'
    }
    POST_DATA = {
        "attributes": [
            {
                "attributeName": "asdf",
                "attributeValue": "Intel® HD Graphics 5300"
            }
        ],
        "categoryId": 2,
        "colors": [
            {
                "code": "C3C3C3",
                "inStock": 10,
                "name": "Gray"
            }
        ],
        "description": "Redesigned with you in mind, the HP Pavilion keeps getting better. Our best-selling notebook is now more powerful so you can watch more, play more, and store more, all in style.",
        "imageUrl": "1100",
        "images": [
            "DD3A5B##1101",
            "DEEE5B##1101"
        ],
        "price": 300,
        "productId": 33,
        "productName": "Notebook",
        "productStatus": "Active"
    }
    response = requests.post(f'{BASE_URL}{POST_URL}', headers=HEADER, json=POST_DATA)
    product_id = response.json()['id']
    yield product_id