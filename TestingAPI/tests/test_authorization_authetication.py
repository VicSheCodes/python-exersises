import pytest
import requests

base_url = 'https://example.com/api'

# credentials for different roles
credentials = {
    'admin': {'username': 'admin@example.com', 'password': 'admin_password'},
    'user': {'username': 'user@example.com', 'password': 'user_password'}
}


@pytest.mark.parametrize("role, expected_status_code", [
    ('admin', 200),
    ('user', 403)
])
def test_authorization_for_role(role, expected_status_code):

    username = credentials[role]['username']
    password = credentials[role]['password']
    token = authenticate(username, password)

    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'{base_url}/restricted_endpoint', headers=headers)

    assert response.status_code == expected_status_code


def authenticate(username, password):
    # Implement authentication logic here send login request and retrieve token

    if username == 'admin@example.com':
        return 'admin_token'
    elif username == 'user@example.com':
        return 'user_token'
    else:
        raise ValueError('Invalid username')
