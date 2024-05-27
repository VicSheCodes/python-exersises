import pytest
import requests

# Define the base URL of the API
base_url = 'https://example.com/api'

# Function to send a GET request to the API
def send_get_request(endpoint, headers=None):
    response = requests.get(f'{base_url}/{endpoint}', headers=headers)
    return response

# Function to send a POST request to the API
def send_post_request(endpoint, data, headers=None):
    response = requests.post(f'{base_url}/{endpoint}', json=data, headers=headers)
    return response

# Test for SQL Injection vulnerability
def test_sql_injection():
    endpoint = 'users'
    malicious_payload = "' OR '1'='1"
    response = send_get_request(f'{endpoint}?username={malicious_payload}')
    assert response.status_code == 400 or response.status_code == 422, "Possible SQL Injection vulnerability"

# Test for Cross-Site Scripting (XSS) vulnerability
def test_xss():
    endpoint = 'users'
    malicious_payload = "<script>alert('XSS')</script>"
    response = send_post_request(endpoint, data={"username": malicious_payload})
    assert malicious_payload not in response.text, "Possible XSS vulnerability"

# Test for Unauthorized Access
def test_unauthorized_access():
    endpoint = 'protected_resource'
    response = send_get_request(endpoint)
    assert response.status_code == 401, "Unauthorized access allowed"

# Test for Privilege Escalation
def test_privilege_escalation():
    endpoint = 'admin_resource'
    headers = {'Authorization': 'Bearer user_token'}  # Token for a regular user
    response = send_get_request(endpoint, headers=headers)
    assert response.status_code == 403, "Privilege escalation vulnerability"

# Test for Sensitive Data Exposure
def test_sensitive_data_exposure():
    endpoint = 'users/1'
    response = send_get_request(endpoint)
    sensitive_fields = ['password', 'ssn', 'credit_card']
    response_data = response.json()
    for field in sensitive_fields:
        assert field not in response_data, f"Sensitive data exposure: {field}"

# Test for Rate Limiting
def test_rate_limiting():
    endpoint = 'users'
    max_requests = 5
    responses = [send_get_request(endpoint) for _ in range(max_requests + 1)]
    assert responses[-1].status_code == 429, "Rate limiting not enforced"

if __name__ == "__main__":
    pytest.main([__file__])
