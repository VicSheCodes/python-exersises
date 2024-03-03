import json
import logging
import uuid
from typing import List, Optional, Tuple, Any

from celery_utils.base_task_with_database import BaseTaskWithDatabase
from celery_utils.db.dal.task import Task
from celery_utils.status_enum import is_completed
from celery_utils.utils import TimeoutException, wait_until

LOGGER = logging.getLogger(__name__)


class BaseGroup:
    def __init__(self) -> None:
        self._group_id = "G-" + str(uuid.uuid4())
        self._tasks_to_run = []
        self._tasks_ids = []

    @property
    def group_id(self) -> str:
        return self._group_id

    def add_task(
        self, task: BaseTaskWithDatabase, *task_args: Any, **task_kwargs: Any
    ) -> None:
        self._tasks_to_run.append((task, task_args, task_kwargs))

    def queue_group(self) -> None:
        for task_num, (task, task_args, task_kwargs) in enumerate(self._tasks_to_run):
            _task = task.queue_group_task(self.group_id, task_args, task_kwargs)
            LOGGER.info("submitting task #%d id=%s", task_num, _task.id)
            self._tasks_ids.append(_task.id)

    def queue_group_and_wait(
        self, timeout: Optional[float] = None, interval: float = 0.5
    ):
        for task, task_args, task_kwargs in self._tasks_to_run:
            _task = task.queue_group_task(self.group_id, task_args, task_kwargs)
            self._tasks_ids.append(_task.id)

        def condition(task_ids=self._tasks_ids) -> bool:
            for task_id in task_ids:
                task_status = Task.get_task_status(task_id)
                if not is_completed(task_status):
                    return False
            return True

        def success_func(
            task_ids=self._tasks_ids,
        ):
            res = []
            for task_id in task_ids:
                res.append(Task.get_task_result(task_id))
            return res

        def failed_func() -> None:
            raise TimeoutException(
                f"Task {task.id} did not complete in {timeout} seconds"
            )

        task_result = wait_until(
            condition, success_func, failed_func, timeout, interval
        )
        return task_result
