from unicodedata import name
import uuid
import uvicorn
import time
import random
import threading

from fastapi import FastAPI

app = FastAPI()
lock = threading.Lock()

db = {}


@app.get("/new/{name}")
@app.post("/new/{name}")
def new_user(name: str):
    time.sleep(5)
    db[name] = {"name": name, "id": f"USER-{uuid.uuid4()}-USER"}
    return "hello " + name


@app.get("/user/{name}/id")
def new_user(name: str):
    time.sleep(2)
    return {name: db[name]["id"]}


@app.get("/user/{id}/age/{age}")
@app.post("/user/{id}/age/{age}")
def set_age(id: str, age: int):
    time.sleep(2)
    for user in db:
        if db[user]["id"] == id:
            db[user]["age"] = age
            return {"id": id, "name": db[user]["name"], "age": age}


@app.get("/user/{name}/add_num/{num}")
@app.post("/user/{name}/add_num/{num}")
def add_num(name: str, num: int):
    time.sleep(random.randint(10, 35) / 10)
    # lock.acquire()
    curr_list = db[name].get("num_list", [])
    curr_list.append(num)
    db[name]["num_list"] = curr_list
    # lock.release()
    return db[name]


@app.get("/user/{name}/num_sum")
def get_sum(name: str):
    time.sleep(1)
    num_list = db[name].get("num_list", [])
    return sum(num_list)


@app.get("/users")
def get_users():
    return {"users": list(db.keys())}


@app.get("/reset")
def reset():
    db.clear()
    return {"message": "db reset"}


@app.get("/")
def main():
    return {"users": db}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8484)
