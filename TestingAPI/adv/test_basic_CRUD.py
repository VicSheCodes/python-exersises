import pytest
import requests

# Define the base URL of the API
base_url = 'https://example.com/api'
resource_endpoint = 'resources'

# Define headers, e.g., for authentication and content type
headers = {
    'Authorization': 'Bearer your_token_here',  # Replace with your actual token
    'Content-Type': 'application/json'
}

# Helper function to create a resource
def create_resource(data):
    response = requests.post(f'{base_url}/{resource_endpoint}', json=data, headers=headers)
    return response

# Helper function to read a resource
def read_resource(resource_id):
    response = requests.get(f'{base_url}/{resource_endpoint}/{resource_id}', headers=headers)
    return response

# Helper function to update a resource
def update_resource(resource_id, data):
    response = requests.put(f'{base_url}/{resource_endpoint}/{resource_id}', json=data, headers=headers)
    return response

# Helper function to delete a resource
def delete_resource(resource_id):
    response = requests.delete(f'{base_url}/{resource_endpoint}/{resource_id}', headers=headers)
    return response

# Test to create a new resource
def test_create_resource():
    data = {
        "name": "Test Resource",
        "description": "This is a test resource"
    }
    response = create_resource(data)
    assert response.status_code == 201, "Failed to create resource"
    response_data = response.json()
    assert response_data['name'] == data['name'], "Resource name does not match"
    assert response_data['description'] == data['description'], "Resource description does not match"

# Test to read an existing resource
def test_read_resource():
    # Assuming a resource with ID 1 exists
    resource_id = 1
    response = read_resource(resource_id)
    assert response.status_code == 200, "Failed to read resource"
    response_data = response.json()
    assert 'name' in response_data, "Resource name not found"
    assert 'description' in response_data, "Resource description not found"

# Test to update an existing resource
def test_update_resource():
    # Assuming a resource with ID 1 exists
    resource_id = 1
    updated_data = {
        "name": "Updated Resource",
        "description": "This is an updated resource"
    }
    response = update_resource(resource_id, updated_data)
    assert response.status_code == 200, "Failed to update resource"
    response_data = response.json()
    assert response_data['name'] == updated_data['name'], "Resource name does not match"
    assert response_data['description'] == updated_data['description'], "Resource description does not match"

# Test to delete an existing resource
def test_delete_resource():
    # Assuming a resource with ID 1 exists
    resource_id = 1
    response = delete_resource(resource_id)
    assert response.status_code == 204, "Failed to delete resource"
    # Verify the resource no longer exists
    response = read_resource(resource_id)
    assert response.status_code == 404, "Resource was not deleted"

if __name__ == "__main__":
    pytest.main([__file__])
