import requests


class RequestsEx():

    def __init__(self):
        self.url = 'https://api.github.com'
        self.invalid_url = 'https://api.github.com/invalid-url'
        pass

    def print_response(self):
        response = requests.get(self.url)
        print(f" \nThe url is: {response.url}")
        print(f"The status code is: {response.status_code}")
        print(f"The headers are: {response.headers}")
        print(f"The content is: {response.content}")
        print(f"The encoding is: {response.encoding}")
        print(f"The cookies are: {response.cookies.items()}")

        return response

    def passing_parameters(self):
        response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests'})
        print(f" \nThe url with parameters is: {response.url}")

    def handle_errors(self):
        response = requests.get(self.invalid_url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f" \nThe error status is: {err.response.status_code}")

    def post_request(self):
        response = requests.post('https://httpbin.org/post', data={'key': 'value'})
        print(f" \nThe response text after post request is: {response.text}")  # Response text
        print(f" \nThe response content after post request is: {response.content}")  # Response content

    def adding_headers(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get('https://api.github.com', headers=headers)
        print(f" \nThe response text after adding headers is: {response.text}")  # Response text
        print(f" \nThe response content after adding headers is: {response.content}")  # Response content

    def authentication(self):
        response = requests.get('https://api.github.com/user', auth=('username', 'password'))
        print(f" \nThe response text after authentication is: {response.json()}")  # Response

    def session(self):
        session = requests.Session()
        response = session.get('https://api.github.com/user', auth=('username', 'password'))
        print(f" \nThe response text after session is: {response.json()}")  # Response


if __name__ == '__main__':
    requests_ex = RequestsEx()
    requests_ex.print_response()
    requests_ex.passing_parameters()
    requests_ex.handle_errors()
    requests_ex.post_request()
    requests_ex.adding_headers()
    requests_ex.authentication()
    requests_ex.session()