
import requests
import time


base_url = 'https://example.com/api'


credentials = {
    'username': 'test_user',
    'password': 'test_password'
}


def generate_token():

    auth_response = requests.post(f'{base_url}/login', json=credentials)

    if auth_response.status_code == 200:
        token = auth_response.json().get('token')
        return token
    else:
        raise ValueError('Authentication failed')


def test_token_expiration():
    token = generate_token()

    # expiration time is 1 second
    time.sleep(2)

    #  use the expired token to access a restricted endpoint
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{base_url}/restricted_endpoint', headers=headers)

    assert response.status_code == 401

