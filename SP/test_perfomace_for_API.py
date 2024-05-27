import pytest
import requests
import time
import concurrent.futures

# Define the base URL of the API
base_url = 'https://example.com/api'

# Function to send a GET request to the API and return response status code and response time
def send_request(endpoint):
    start_time = time.time()
    response = requests.get(f'{base_url}/{endpoint}')
    end_time = time.time()
    return response.status_code, end_time - start_time

# Test to simulate load on the API and measure performance
def test_performance():
    # Define the number of concurrent users and endpoints to be tested
    num_users = 50
    endpoints = ['endpoint1', 'endpoint2', 'endpoint3']  # Add more endpoints as needed

    # Create a ThreadPoolExecutor with the number of users as max_workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_users) as executor:
        # Submit requests to the API concurrently and get results
        results = list(executor.map(send_request, endpoints * num_users))

    # Extract status codes and response times
    status_codes = [result[0] for result in results]
    response_times = [result[1] for result in results]

    # Assert that all responses are successful (status code 200)
    assert all(status_code == 200 for status_code in status_codes)

    # Calculate performance metrics
    total_requests = len(results)
    avg_response_time = sum(response_times) / total_requests
    max_response_time = max(response_times)
    min_response_time = min(response_times)

    # Print performance metrics
    print(f'Total Requests: {total_requests}')
    print(f'Average Response Time: {avg_response_time:.2f} seconds')
    print(f'Max Response Time: {max_response_time:.2f} seconds')
    print(f'Min Response Time: {min_response_time:.2f} seconds')

    # Assert acceptable performance thresholds (adjust thresholds as needed)
    assert avg_response_time < 1.0  # Example threshold for average response time
    assert max_response_time < 2.0  # Example threshold for maximum response time

if __name__ == "__main__":
    pytest.main([__file__])
