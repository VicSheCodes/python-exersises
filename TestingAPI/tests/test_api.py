import pytest
import requests
import json
import os

# Load configuration

with open(os.path.join(os.path.dirname(os.getcwd()), 'config.json')) as config_file:
    config = json.load(config_file)
base_url = config['base_url']
credentials = config['credentials']


@pytest.mark.parametrize("endpoint, expected_key, expected_value", [
    ("/api/users/?page=2", "page", 2),
    ("/api/users/?page=1", "page", 1),
    # ("/api/users/1", "id", "1"),
    # Add more combinations as needed
])
def test_get_endpoint(endpoint, expected_key, expected_value, base_url=base_url):
    full_endpoint = f"{base_url}{endpoint}"
    response = requests.get(full_endpoint)

    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']

    data = response.json()
    print(data)
    for k in data.keys():
        print(k)
        print(data[k])
    assert expected_key in data.keys()
    assert data[expected_key] == expected_value


@pytest.mark.parametrize("endpoint, expected_key, second_key, expected_value", [
    ("/api/users/1", "data", "id", 1),
])
def test_verify_key(endpoint, expected_key, second_key, expected_value, base_url=base_url):
    full_endpoint = f"{base_url}{endpoint}"
    response = requests.get(full_endpoint)

    assert response.status_code == 200
    assert 'application/json' in response.headers['Content-Type']

    data = response.json()
    assert expected_key in data
    assert second_key in data[expected_key]
    assert data[expected_key][second_key] == expected_value


@pytest.mark.parametrize("endpoint, key1, value1, key2, value2", [
    ("/api/users", "name", "morpheus", "job", "leader"),
])
def test_post_endpoint(endpoint, key1, value1, key2, value2, base_url=base_url):
    endpoint = f"{base_url}{endpoint}"
    payload = {
        key1: value1,
        key2: value2
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(endpoint, data=json.dumps(payload), headers=headers)

    assert response.status_code == 201
    assert 'application/json' in response.headers['Content-Type']

    data = response.json()
    print(data)
    assert data[key1] == value1
    assert data[key2] == value2


def test_user_not_found(base_url=base_url):
    endpoint = f"{base_url}/api/users/23"
    response = requests.get(endpoint)

    assert response.status_code == 404

    data = response.json()
    assert data == {}


def test_register(base_url=base_url):
    endpoint = f"{base_url}/api/register"

    response = requests.post(endpoint, data=credentials)

    assert response.status_code == 200
    response_data = response.json()

    assert 'id' in response_data.keys()
    assert 'token' in response_data.keys()
    token = response_data['token']
    id = response_data['id']


def test_login(base_url=base_url):
    endpoint = f"{base_url}/api/login"

    response = requests.post(endpoint, data=credentials)

    assert response.status_code == 200
    response_data = response.json()
    token = response.json().get('token')
    # token = response_data['token']
    print(token)

    assert 'id' not in response_data.keys()
    assert 'token' in response_data.keys()


def login(base_url=base_url):
    response = requests.post(f"{base_url}/api/login", data=credentials)
    assert response.status_code == 200
    return response.json().get('token')


def logout(base_url=base_url):
    response = requests.post(f"{base_url}/api/logout")
    assert response.status_code == 200


def test_logout():
    token = login()
    print(token)
    # headers = {'Authorization': f'Bearer {token}'}
    # headers = {'accept: */*'}
    # response = requests.post(f"{base_url}/api/logout", headers=headers)
    response = requests.post(f"{base_url}/api/logout", )
    assert response.status_code == 200


class OrbitraryTests():

    def test_simultaneous_sessions(self):
        # Log in to create two sessions simultaneously
        token1 = login()
        token2 = login()

        headers1 = {'Authorization': f'Bearer {token1}'}
        headers2 = {'Authorization': f'Bearer {token2}'}

        response1 = requests.get(f"{base_url}/api/users/2", headers=headers1)
        response2 = requests.get(f"{base_url}/api/users/2", headers=headers2)

        assert response1.status_code == 200
        assert response2.status_code == 200

    def test_session_reopen(self):
        # Log in to create a session
        token = login()

        headers = {'Authorization': f'Bearer {token}'}

        # Ensure the token is valid
        response = requests.get(f"{base_url}/api/users/2", headers=headers)
        assert response.status_code == 200

        # Close the session (not logging out)
        # Simulate closing the session by just reusing the token after a break

        # Reopen the session (reusing the token)
        response = requests.get(f"{base_url}/api/users/1", headers=headers)
        assert response.status_code == 200

        # Cleanup: Log out
        logout()

    def test_session_invalid_after_logout(self):
        # Log in to create a session
        token = login()

        headers = {'Authorization': f'Bearer {token}'}

        # Ensure the token is valid
        response = requests.get(f"{base_url}/api/users/1", headers=headers)
        assert response.status_code == 200

        # Log out to invalidate the token
        logout()

        # Attempt to reuse the invalidated token
        response = requests.get(f"{base_url}/api/users/1", headers=headers)
        assert response.status_code == 401  # Unauthorized

    def test_multiple_session_handling_after_logout(self):
        # Log in to create two sessions simultaneously
        token1 = login()
        token2 = login()

        headers1 = {'Authorization': f'Bearer {token1}'}
        headers2 = {'Authorization': f'Bearer {token2}'}

        # Ensure both tokens are valid
        response1 = requests.get(f"{base_url}/users/me", headers=headers1)
        response2 = requests.get(f"{base_url}/users/me", headers=headers2)

        assert response1.status_code == 200
        assert response2.status_code == 200

        # Log out from one session
        logout(token1)

        # The other session should still be valid
        response2 = requests.get(f"{base_url}/users/me", headers=headers2)
        assert response2.status_code == 200

        # Cleanup: Log out the second session
        logout(token2)

    def test_rate_limit_exceeded(self, base_url=base_url):
        endpoint = f"{base_url}/api/some_endpoint"

        #  exit if exceed the rate limit = 101 per minute exceeded
        for _ in range(101):
            response = requests.get(endpoint)
            if response.status_code != 200:
                break

                # ast response is a rate limit exceeded error
        assert response.status_code == 429
        assert 'Retry-After' in response.headers

    # More test functions as needed...

def test_authorization_for_role(base_url=base_url):
    pass