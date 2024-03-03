from tasks import register_new_user


def old_main():
    from tasks import add

    add_task = add.delay(1, 2)
    print("add_task.id: {}".format(add_task.id))


def main():
    # TODO: add your code here
    task1 = register_new_user.delay('Roy')
    task2 = register_new_user.delay('Vika')


if __name__ == "__main__":
    main()
