import logging
import typing

import celery
import uuid

from kombu import serialization
from celery.signals import after_setup_logger, setup_logging

from celery_utils.base_app_with_database import BaseAppWithDatabase
from celery_utils.db.dal.task import Task
from celery_utils.status_enum import Status, is_completed
from celery_utils.utils import wait_until, TimeoutException


class BaseTaskWithDatabaseException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BaseTaskWithDatabase(celery.Task):  # type: ignore[misc]
    """A base class for celery tasks, the tasks statuses and result will be saved to the database"""

    def __init__(self, **kwargs) -> None:
        # getting the save_extra flag from the task decorator
        self.save_extra = kwargs.pop("save_extra", True)

    @classmethod
    def bind(cls, app: celery.Celery) -> celery.Celery:
        if not isinstance(app, BaseAppWithDatabase):
            raise BaseTaskWithDatabaseException(
                "celery app must be an instance of BaseAppWithDatabase"
            )
        return super().bind(app)

    def queue_group_task(self, group_id, args, kwargs) -> celery.result.AsyncResult:
        task = self.apply_async(args=args, kwargs=kwargs, group_id=group_id)
        return task

    def queue_task(self, *args, **kwargs) -> celery.result.AsyncResult:
        """Add task to celery task queue"""
        task = self.apply_async(args=args, kwargs=kwargs)  # ,group_id=group_id)
        return task

    def queue_task_and_wait(
        self,
        *args,
        interval: float = 0.5,
        timeout: typing.Optional[float] = None,
        **kwargs,
    ) -> celery.result.AsyncResult:
        """Add task to celery task queue and wait for it to complete, returns task_id and result"""
        task = self.queue_task(*args, **kwargs)

        def condition(task_id=task.id) -> bool:
            return is_completed(self._get_task_status(task_id))

        def success_func(task_id=task.id):
            return self._get_task_result(task_id)

        def failed_func(
            task_id=task.id, timeout: typing.Optional[float] = timeout
        ) -> None:
            raise TimeoutException(
                f"Task {task_id} did not complete in {timeout} seconds"
            )

        task_result = wait_until(
            condition, success_func, failed_func, timeout, interval
        )
        return task

    # TODO: current method signature is same as in parent class, maybe add type hints.
    def apply_async(
        self,
        args=None,  # type: ignore[no-untyped-def]
        kwargs=None,
        task_id=None,
        producer=None,
        link=None,
        link_error=None,
        shadow=None,
        *,
        group_id=None,
        **options,
    ) -> celery.result.AsyncResult:
        # full celery signature for backward compatibility

        if task_id is None:
            task_id = str(uuid.uuid4())
        if group_id is None:
            group_id = task_id

        self._create_task_in_db(
            task_id=task_id,
            group_id=group_id,
            task_function_name=self.name,
            task_args=args,
            task_kwargs=kwargs,
        )

        Task.update_task_status(task_id=task_id, status=Status.CREATED)
        return super().apply_async(
            args, kwargs, task_id, producer, link, link_error, shadow, **options
        )

    # TODO: current method signature is same as in parent class, maybe add type hints.
    def apply(
        self,
        args=None,
        kwargs=None,
        link=None,
        link_error=None,  # type: ignore[no-untyped-def]
        task_id=None,
        retries=None,
        throw=None,
        logfile=None,
        loglevel=None,
        headers=None,
        group_id=None,
        **options,
    ) -> celery.result.EagerResult:
        # full celery signature for backward compatibility

        if task_id is None:
            task_id = str(uuid.uuid4())
        if group_id is None:
            group_id = task_id

        self._create_task_in_db(
            task_id=task_id,
            group_id=group_id,
            task_function_name=self.name,
            task_args=args,
            task_kwargs=kwargs,
        )
        return super().apply(
            args,
            kwargs,
            link,
            link_error,
            task_id,
            retries,
            throw,
            logfile,
            loglevel,
            headers,
            group_id=group_id,
            **options,
        )

    def update_status(self, new_status: Status) -> None:
        Task.update_task_status(task_id=self.request.id, status=new_status)

    def update_result(self, retval) -> None:
        _, _, resval_serialized = serialization.dumps(retval)
        Task.update_task_result(task_id=self.request.id, result=resval_serialized)

    def on_success(
        self,
        retval,
        task_id,
        *args,
        **kwargs,
    ) -> None:
        self.update_result(retval)
        self.update_status(Status.SUCCESS)

    def on_failure(
        self,
        exc: Exception,
        task_id,
        args,
        kwargs,
        einfo: str,
    ) -> None:
        failure_message = {"exception": str(exc)}
        if self.save_extra:
            failure_message["einfo"] = str(einfo)
        self.update_result(failure_message)
        self.update_status(Status.FAILED)

    def _create_task_in_db(
        self,
        task_id,
        group_id,
        task_function_name: str,
        task_args=None,
        task_kwargs=None,
    ) -> None:
        args_serialized, kwargs_serialized = None, None
        if self.save_extra:
            _, _, args_serialized = serialization.dumps(task_args)
            _, _, kwargs_serialized = serialization.dumps(task_kwargs)

        Task.create_task(
            task_id=task_id,
            group_id=group_id,
            task_function_name=task_function_name,
            task_args=args_serialized,
            task_kwargs=kwargs_serialized,
        )

    @staticmethod
    def _get_task_status(task_id) -> Status:
        return Task.get_task_status(task_id)

    @staticmethod
    def _get_task_result(task_id):
        return Task.get_task_result(task_id)

    @property
    def group_id(self):
        task_id = self.request.id
        return Task.get_task_group_id(task_id)


@celery.signals.task_prerun.connect  # type: ignore[misc]
def on_task_prerun(task_id, task: celery.Task, *args, **kwargs) -> None:
    if isinstance(task, BaseTaskWithDatabase):
        Task.update_task_status(task_id=task_id, status=Status.STARTED)
