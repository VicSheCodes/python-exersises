import json
import logging

from celery import Celery
from typing import List, Union

from celery_utils.db import set_db_url
from celery_utils.db.dal.task import Task
from celery_utils.celery_config import CeleryConfig
from celery_utils.status_enum import Status

LOGGER = logging.getLogger(__name__)


class BaseAppWithDatabase(Celery):  # type: ignore[misc]
    """wrapper around celery app that sets up the database connection and allow getting Task data"""

    def __init__(self, celery_config: CeleryConfig, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_from_object(celery_config)

        # this assert there is an engine and a session can be created
        set_db_url(celery_config.database_url)

    def start_worker(self, *args: str) -> None:
        argv = [
            "worker",
        ]
        argv.extend(args)
        LOGGER.info("Starting celery worker with args: %s", argv)
        self.worker_main(argv)

    def get_task_status(self, task_id) -> Status:
        return Task.get_task_status(task_id)

    def get_task_result(self, task_id):
        return Task.get_task_result(task_id)

    def get_group_tasks(self, group_id):
        group_tasks = Task.get_tasks_by_group_id(group_id)
        tasks_ids = [task.task_id for task in group_tasks]
        return tasks_ids

    # job is a set of tasks -> job == group (may be a single task in group)

    def get_job_status(self, job_id) -> List[Status]:
        group_tasks = Task.get_tasks_by_group_id(job_id)
        statuses = [task.status for task in group_tasks]
        return statuses

    def get_job_results(self, job_id):
        group_tasks = Task.get_tasks_by_group_id(job_id)
        results = [task.result for task in group_tasks]
        return results
