import requests

base_url = 'https://example.com/api'


# 404 Not Found error
def test_404_error():
    response = requests.get(f'{base_url}/nonexistent_endpoint')
    assert response.status_code == 404


# 400 Bad Request error
def test_400_error():
    response = requests.post(f'{base_url}/invalid_endpoint')
    assert response.status_code == 400


# 401 Unauthorized error
def test_401_error():
    response = requests.get(f'{base_url}/restricted_endpoint')
    assert response.status_code == 401


# 403 Forbidden error
def test_403_error():
    response = requests.get(f'{base_url}/forbidden_endpoint')
    assert response.status_code == 403


# 500 Internal Server Error
def test_500_error():
    response = requests.get(f'{base_url}/error_endpoint')
    assert response.status_code == 500


# error message in response body
def test_error_message():
    response = requests.get(f'{base_url}/nonexistent_endpoint')
    assert 'Endpoint not found' in response.text
