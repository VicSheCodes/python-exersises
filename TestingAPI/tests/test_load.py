import requests
import concurrent.futures

base_url = 'https://example.com/api'


def send_request(endpoint):
    response = requests.get(f'{base_url}/{endpoint}')
    return response.status_code


def test_load():
    concurrent_users = 10
    endpoints = ['endpoint1', 'endpoint2', 'endpoint3']

    # Create a ThreadPoolExecutor with the number of users as max_workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_users) as executor:
        results = list(executor.map(send_request, endpoints * concurrent_users))

    assert all(result == 200 for result in results)
