from our_celery_app import app
import requests
import time, requests
from our_celery_app import app

# api-endpoints
URL1 = "http://localhost:8484/new/{name}"
URL2 = "http://localhost:8484/user/{name}/id"
URL3 = "http://localhost:8484/user/{id}/age/{age}"
URL4 = "http://localhost:8484/user/{name}/add_num/{num}"

@app.task
def mul(x, y):
    time.sleep(2)
    return x * y


@app.task
def add(x, y):
    time.sleep(2)
    return x + y


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

@app.task
def set_user_age_by_id(id, age):
    print("Inside set_user_age_by_id task with id: {} and age: {}".format(id, age))
    r = requests.post(url=URL3.format(id=id, age=age))
    data = r.json()
    print(data)
    return data

@app.task
def set_user_numbers(name, num):
    print("Inside set_user_numbers task with name: {} and number: {}".format(name, num))
    r = requests.post(url=URL4.format(name=name, num=num))
    data = r.json()
    print(data)
    return data
