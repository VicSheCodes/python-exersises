from tasks import register_new_user, get_user_id
import time



def old_main():
    import time
    from tasks import add

    add_task = add.delay(1, 2)
    print("add_task.id: {}".format(add_task.id))
    print(add_task.get())

    # OR

    add_task = add.delay(1, 2)
    print("add_task.id: {}".format(add_task.id))
    while add_task.status != "SUCCESS":
        print("add_task.status: {}".format(add_task.status))
        time.sleep(1)
    print("add_task.result: {}".format(add_task.result))


def main():
    task1 = register_new_user.delay('Roy')
    print("register_new_user.id: {}".format(task1.id))
    # The ready() method returns whether the task has finished processing or not:
    print("register_new_user is ready: {}".format(task1.ready()))

    while task1.status != "SUCCESS":
        print("register_new_user.status: {}".format(task1.status))
        time.sleep(1)

    print("register_new_user task is ready: {}".format(task1.ready()))
    print("register_new_user task's status: {}".format(task1.status))
    print("register_new_user.result: {}".format(task1.result))

    task1_result = task1.get()
    print("register_new_user.get: {}".format(task1_result))

    # task2 = register_new_user.delay('Vika')
    # print("register_new_user.id: {}".format(task2.id))
    # print("register_new_user.result: {}".format(task2.result))

    if task1.status == "SUCCESS":
        task3 = get_user_id.delay('Roy')
        while task3.status != "SUCCESS":
            print("get_user_id.status: {}".format(task3.status))
            time.sleep(1)

        task3_result = task3.get()
        print("get_user_id.id: {}".format(task3.id))
        print("get_user_id task is ready: {}".format(task1.ready()))
        print("get_user_id.result: {}".format(task3_result))

    pass

if __name__ == "__main__":
    main()
