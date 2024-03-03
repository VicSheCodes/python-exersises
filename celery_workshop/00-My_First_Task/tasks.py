from our_celery_app import app
import requests


@app.task
def add(x, y):
    print("add {} + {}".format(x, y))
    time.sleep(5)
    return x + y


# TODO: add your code here
# api-endpoint
URL = "http://localhost:8484/new/{name}"

@app.task
def register_new_user(name):
    r = requests.post(url=URL.format(name=name))
    print(r)


