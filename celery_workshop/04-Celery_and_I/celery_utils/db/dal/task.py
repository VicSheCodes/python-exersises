import json

from sqlalchemy.orm import Session
from typing import Optional, List

from celery_utils.db import get_session
from celery_utils.db.tables.task_table import TaskTable
from celery_utils.db.tables.task_result import TaskResultTable

from celery_utils.status_enum import Status


class TaskNotFound(Exception):
    def __init__(self, task_id):
        super().__init__(f"Task with id {task_id} not found")


class Task:
    """This (dal) class is used to store and retrieve information about a task from the task_table."""

    @classmethod
    def check_session(cls) -> None:
        print(cls.session.execute("Select Version()").fetchall())  # type: ignore[attr-defined]

    @classmethod
    @property
    def session(cls) -> Session:
        return get_session()

    @classmethod
    def get_task(cls, task_id) -> TaskTable:
        session: Session = cls.session  # type: ignore[assignment]

        task: Optional[TaskTable] = (
            session.query(TaskTable).filter(TaskTable.task_id == task_id).first()
        )
        if not task:
            raise TaskNotFound(task_id)
        return task

    @classmethod
    def get_tasks_by_group_id(cls, group_id) -> List[TaskTable]:
        session: Session = cls.session  # type: ignore[assignment]
        return session.query(TaskTable).filter(TaskTable.group_id == group_id).all()

    @classmethod
    def create_task(
        cls,
        task_id,
        group_id,
        task_function_name: str,
        task_args,
        task_kwargs,
    ) -> TaskTable:
        task = TaskTable(
            task_id=task_id,
            group_id=group_id,
            status=Status.CREATED,
            task_function_name=task_function_name,
            args=task_args,
            kwargs=task_kwargs,
        )

        task_result = TaskResultTable(task_id=task_id, result=None)

        session: Session = cls.session  # type: ignore[assignment]
        session.add(task)
        session.add(task_result)
        session.commit()
        return task

    @classmethod
    def update_task_group(cls, task_id, group_id) -> TaskTable:
        task = cls.get_task(task_id)
        task.group_id = group_id

        session = Session.object_session(task)
        session.add(task)
        session.commit()
        return task

    @classmethod
    def update_task_status(cls, task_id, status: Status) -> TaskTable:
        task = cls.get_task(task_id)
        task.status = status

        session = Session.object_session(task)
        session.add(task)
        session.commit()
        return task

    @classmethod
    def update_task_result(cls, task_id, result) -> TaskTable:
        task = cls.get_task(task_id)
        task.task_result.result = result

        session = Session.object_session(task)
        session.add(task)
        session.commit()
        return task

    @classmethod
    def get_task_status(cls, task_id) -> Status:
        task = cls.get_task(task_id)
        return task.status

    @classmethod
    def get_task_result(cls, task_id):
        task = cls.get_task(task_id)
        return task.result

    @classmethod
    def get_task_group_id(cls, task_id):
        task = cls.get_task(task_id)
        group_id = task.group_id or task_id
        return group_id
