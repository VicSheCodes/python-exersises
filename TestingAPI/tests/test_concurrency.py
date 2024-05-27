import requests
import concurrent.futures

base_url = 'https://example.com/api'


def send_request(endpoint):
    response = requests.get(f'{base_url}/{endpoint}')
    return response.status_code


# simulate concurrent requests
def test_concurrency():
    # endpoints to be tested concurrently
    endpoints = ['endpoint1', 'endpoint2', 'endpoint3']

    # Create a ThreadPoolExecutor with 5 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Submit requests to the API concurrently and get results
        results = list(executor.map(send_request, endpoints))

    # Assert that all responses are successful (status code 200)
    assert all(result == 200 for result in results)
