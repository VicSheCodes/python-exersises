import requests
import os

print(os.environ)
GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')


def get_search_query():
    return input("Enter your search query (leave blank to view your GitHub profile): ")


def do_github_repository_search():
    search_query = get_search_query()

    if search_query:
        url = 'https://api.github.com/search/repositories'
        params = {'q': search_query}
        headers = {'Authorization': 'Bearer ' + GITHUB_ACCESS_TOKEN}
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            repositories = data['items'][:5]
            for repo in repositories:
                print(f"Repository: {repo['name']}, URL: {repo['html_url']}")
        else:
            print(f"Failed to retrieve repositories. Status code: {response.status_code}")

    else:
        url = 'https://api.github.com/user'
        headers = {'Authorization': 'Bearer ' + GITHUB_ACCESS_TOKEN}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            profile_data = response.json()
            print("GitHub Profile Information:")
            print(f"Username: {profile_data['login']}")
            print(f"Name: {profile_data['name']}")
            print(f"Email: {profile_data['email']}")
        else:
            print(f"Failed to retrieve profile information. Status code: {response.status_code}")


if __name__ == '__main__':
    do_github_repository_search()
