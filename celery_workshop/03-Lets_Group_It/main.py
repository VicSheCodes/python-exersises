from tasks import register_new_user, get_user_id, set_user_age_by_id, set_user_numbers
from celery import chain, group
import time


def old_main():
    from tasks import add, mul
    import time

    c = chain(add.s(5, 5), add.s(10), mul.si(5, 20), mul.s(10))
    task_c = c.delay()
    task_res = task_c.get()
    print(task_res)

    g = group(add.s(5, 5), add.s(10, 10), mul.si(5, 20), mul.s(10, 10))
    task_g = g()
    print(task_g.completed_count())
    time.sleep(3)
    print(task_g.completed_count())

    group_res = task_g.get()
    print(group_res)
    print(task_g.completed_count())


def main():
    c = chain(register_new_user.s("Che"), get_user_id.si("Che"), set_user_age_by_id.s(age=18))
    task_c = c.delay()
    task_res = task_c.get()
    print("task_c status {}".format(task_c.status))
    print("task_c result {}".format(task_res))

    c2 = chain(register_new_user.s("Vika"), get_user_id.si("Vika"), set_user_age_by_id.s(age=99))
    task_c2 = c2()
    print("task_c2 status {}".format(task_c2.status))
    task_c2_res = task_c2.get()
    print("task_c2 status {}".format(task_c2.status))
    print("task_c2 result {}".format(task_c2_res))

    job = group(set_user_numbers.s("Che", 11), set_user_numbers.s("Che", 2), set_user_numbers.s("Vika", 3),
                 set_user_numbers.s("Vika", 100))
    result = job.delay()
    print(result.ready())
    print(result.successful())
    r = result.get()
    print(result.successful())
    print(r)
    pass


if __name__ == "__main__":
    main()
