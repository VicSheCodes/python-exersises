from our_celery_app import app
import requests
import time


@app.task
def add(x, y):
    print("add {} + {}".format(x, y))
    time.sleep(5)
    return x + y


# api-endpoint
URL1 = "http://localhost:8484/new/{name}"
URL2 = "http://localhost:8484/user/{name}/id"

@app.task
def register_new_user(name):
    r = requests.post(url=URL1.format(name=name))
    print(r)


@app.task
def get_user_id(name):
    print("Inside get_user_id task with name: {}".format(name))
    r = requests.get(url=URL2.format(name=name))
    # extracting data in json format
    data = r.json()
    print(data['{}'.format(name)])
    return data['{}'.format(name)]
