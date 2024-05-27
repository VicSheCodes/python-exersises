import pytest
import requests

base_url = 'https://example.com/api'
resource_endpoint = 'resources'

# Define headers, e.g., for authentication and content type
headers = {
    'Authorization': 'Bearer your_token_here',  # Replace with your actual token
    'Content-Type': 'application/json'
}

@pytest.fixture(scope="module")
def create_resource():
    # Fixture to create a resource
    def _create_resource(data):
        response = requests.post(f'{base_url}/{resource_endpoint}', json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()

    return _create_resource

@pytest.fixture(scope="module")
def delete_resource():
    # Fixture to delete a resource
    def _delete_resource(resource_id):
        response = requests.delete(f'{base_url}/{resource_endpoint}/{resource_id}', headers=headers)
        response.raise_for_status()
        return response

    return _delete_resource

@pytest.fixture
def resource(create_resource, delete_resource):
    # Create a new resource before each test and delete it after
    data = {
        "name": "Test Resource",
        "description": "This is a test resource"
    }
    resource = create_resource(data)
    yield resource
    delete_resource(resource['id'])
