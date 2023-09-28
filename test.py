import requests
from pprint import pprint

def test1():
    url = 'https://www.advantageonlineshopping.com/catalog/api/v1/products/35'
    response = requests.get(url)
    pprint(response.json())
    print()
    print(f'Status code: {response.status_code}')


def test_second():
    pass