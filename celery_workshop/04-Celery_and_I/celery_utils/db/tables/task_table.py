import json
from datetime import datetime
from sqlalchemy import Column, DateTime, JSON, String, Enum
from sqlalchemy.orm import relationship

from celery_utils.status_enum import Status
from ._base import BaseTable
from .task_result import TaskResultTable


class TaskTable(BaseTable):
    __tablename__ = "task"

    task_id = Column(String, primary_key=True)
    group_id = Column(String, index=True)

    status: Status = Column(
        Enum(Status), default=Status.PENDING, nullable=False, index=True
    )

    created_at: datetime = Column(
        DateTime, nullable=False, default=datetime.utcnow, index=True
    )
    updated_at: datetime = Column(
        DateTime,
        nullable=False,
        onupdate=datetime.utcnow,
        default=datetime.utcnow,
        index=True,
    )

    task_function_name: str = Column(String, index=True)
    args = Column(JSON)
    kwargs = Column(JSON)

    task_result: TaskResultTable = relationship(
        "TaskResultTable", backref="task", uselist=False
    )

    def __repr__(self) -> str:
        return (
            f"<Task(task_id='{self.task_id}', "
            f"group_id='{self.group_id}', "
            f"status='{self.status}', "
            f"created_at='{self.created_at}', "
            f"updated_at='{self.updated_at}')>"
        )

    @property
    def result(self):
        result = json.loads(self.task_result.result)  # type: ignore[arg-type]
        return result
