import json

import requests

BASE_LINK = "https://reqres.in"
UNIQUE_ID_COUNTER = 13


class User:

    def __init__(self, data):
        self.link = f"{BASE_LINK}/api/users"
        self.id = data.get('id', None)
        self.email = data.get('email', None)
        self.name = data.get('name', None)
        self.last_name = data.get('last_name', None)
        self.job = data.get('job', None)
        self.avatar = data.get('avatar', None)

    def print_user(self):
        print(f"ID: {self.id}")
        print(f"Email: {self.email}")
        print(f"First Name: {self.name}")
        print(f"Last Name: {self.last_name}")
        print(f"Avatar: {self.avatar}")
        print(f"Job: {self.job}")
        print(f"Link: {self.link}")

    def create_user(self):
        data = {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "job": self.job,
            "avatar": self.avatar,
            "link": self.link
        }
        headers = {"Content-Type": "application/json"}

        response = requests.post(self.link, headers=headers, data=json.dumps(data))
        if response.status_code == 201:
            return response.json()
        return


class ManageUsers:
    def __init__(self):
        self.base_link = f"{BASE_LINK}/api/users"

    def get_user(self, id):
        link = f"{self.base_link}/{id}"

        response = requests.get(link)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to retrieve users. Status code: {response.status_code}")
            return None

    def update_user(self, data):
        link = f"{self.base_link}/2"
        headers = {"Content-Type": "application/json"}

        response = requests.put(link, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to update users. Status code: {response.status_code}")
            return response.status_code

    def delete(self):
        link = f"{self.base_link}/2"

        response = requests.delete(link)
        if response.status_code == 204:
            print("Deleted successfully!")
            return response.status_code
        else:
            print(f"Failed to update users. Status code: {response.status_code}")
            return response.status_code


class ManageApi:
    def __init__(self):
        self.base_link = f"{BASE_LINK}/api"

    def register(self, email, password = None):
        link = f"{self.base_link}/register"

        data = {"email": email, "password": password}

        response = requests.post(link, json=data)

        if response.status_code == 200:
            response_data = response.json()
            user_id = response_data["id"]
            token = response_data["token"]
            print("User registered successfully!")
            print("User ID:", user_id)
            print("Token:", token)
        else:
            print(f"Failed to register user. Status code: {response.status_code}")
            print("Response:", response.text)


    # def get_user(self, id):
    #     link = f"{self.link}/{id}"
    #     response = requests.get(link)
    #
    #     if response.status_code == 200:
    #         return response.json()
    #     else:
    #         print(f"Failed to retrieve users. Status code: {response.status_code}")
    #         return None
    #
    # def get_user_pretty(self, id):
    #     pretty_json = json.dumps(self.get_user(id), indent=4)
    #
    #     if pretty_json:
    #         return pretty_json
    #     else:
    #         print(f"Failed to retrieve user {id}.")
    #         return None
    #
    # #
    # # def update_user(self, data):
    # #
    # #     response = requests.put(self.link)
    # #
    # #     if response.status_code == 200:
    # #         return response.json()
    # #     else:
    # #         print(f"Failed to update users. Status code: {response.status_code}")
    # #         return None
    # #
    # # def delete_user(self, id):
    # #
    # #     response = requests.delete(self.link)
    # #
    # #     if response.status_code == 200:
    # #         return response.json()
    # #     else:
    # #         print(f"Failed to delete users. Status code: {response.status_code}")
    # #         return None
    # #
    # def create_user(self, data):
    #     body = json.dumps(data)
    #     print(f"body {body}")
    #     response = requests.post(self.link, data=body)
    #
    #     if response.status_code == 201:
    #         response_data = response.json()
    #         new_user_id = response_data.get('id', None)
    #         print(f"new user data {response_data}")
    #         return response.json()
    #     else:
    #         print(f"Failed to create user. Status code: {response.status_code}")
    #         return None
    #


if __name__ == "__main__":
    user = User({"id": 7, "email": "<EMAIL>", "name": "Michael", "last_name": "Lawson",
                 "avatar": "https://reqres.in/img/faces/7-image.jpg"})
    user_data = {"name": "morpheus", "job": "leader"}
    user_data_2 = {"id": "13",  "name": "neo", "job": "jerk"}
    user_data_3 = {"name": "morpheus", "job": "zion resident"}
    # curl - X POST https: // reqres. in / api / users - H "Content-Type: application/json" - d "{\"name\": \"Eve\", \"job\": \"Holt\"}"

    user_morpheus = User(user_data)
    user_neo = User(user_data_2)
    # print_user = user_morpheus.print_user()
    print(user_morpheus.create_user())
    print(user_neo.create_user())
    do = ManageUsers()
    print(do.get_user(13))
    print(do.get_user(12))
    print(do.update_user(user_data_3))
    print(do.delete())
    manage_api = ManageApi()
    print(manage_api.register("eve.holt@reqres.in", "pistol"))
    print(manage_api.register("eve.holt@reqres.in"))
