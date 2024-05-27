import requests

base_url = 'https://example.com/api'
resource_endpoint = 'resources'

# Define headers, e.g., for authentication and content type
headers = {
    'Authorization': 'Bearer your_token_here',  # Replace with your actual token
    'Content-Type': 'application/json'
}


def test_create_resource(create_resource, delete_resource):
    data = {
        "name": "Another Test Resource",
        "description": "This is another test resource"
    }
    resource = create_resource(data)
    assert resource['name'] == data['name']
    assert resource['description'] == data['description']

    # Cleanup
    delete_resource(resource['id'])


def test_read_resource(resource):
    resource_id = resource['id']
    response = requests.get(f'{base_url}/{resource_endpoint}/{resource_id}', headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['name'] == resource['name']
    assert response_data['description'] == resource['description']


def test_update_resource(resource):
    resource_id = resource['id']
    updated_data = {
        "name": "Updated Resource",
        "description": "This is an updated resource"
    }
    response = requests.put(f'{base_url}/{resource_endpoint}/{resource_id}', json=updated_data, headers=headers)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['name'] == updated_data['name']
    assert response_data['description'] == updated_data['description']


def test_delete_resource(resource):
    resource_id = resource['id']
    response = requests.delete(f'{base_url}/{resource_endpoint}/{resource_id}', headers=headers)
    assert response.status_code == 204

    # Verify the resource no longer exists
    response = requests.get(f'{base_url}/{resource_endpoint}/{resource_id}', headers=headers)
    assert response.status_code == 404
