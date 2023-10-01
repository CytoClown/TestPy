import requests
from pprint import pprint
from data.data import Data
from data.url import Urls
from data.headers import Header

class Test:
    J_data = Data
    base_url = Urls()
    headers = Header()

    def test_token(self):
        response = requests.post(f'{self.base_url.base_url}{self.base_url.token_url}', headers=self.headers.header_token, json=self.J_data.data)
        assert response.status_code == 200, f'Status code is not {response.status_code}'
        pprint(response.json())
        print(f'Status code: {response.status_code}')

    def test_post(self):
        response = requests.post(f'{self.base_url.base_url}{self.base_url.post_url}', headers=self.headers.header_post, json=self.J_data.post_data)
        assert response.status_code == 200, f'Status code is not {response.status_code}'
        pprint(response.json())
        print(f'Status code: {response.status_code}')

    def test_get(self):
        response = requests.get(f'{self.base_url.base_url}{self.base_url.get_url}')
        assert response.status_code == 200, f'Status code is not {response.status_code}'
        print(f'Status code: {response.status_code}')
        pprint(response.json())

    def test_put(self):
        response = requests.put(f'{self.base_url.base_url}{self.base_url.get_url}', headers=self.headers.header_post, json=self.J_data.put_data)
        assert response.status_code == 200, f'Status code is not {response.status_code}'
        print(f'Status code: {response.status_code}')
        pprint(response.json())

    def test_delete(self):
        response = requests.delete(f'{self.base_url.base_url}{self.base_url.delete_url}', headers=self.headers.header_del)
        assert response.status_code == 200, f'Status code is not {response.status_code}'
        print(f'Status code: {response.status_code}')
        pprint(response.json())