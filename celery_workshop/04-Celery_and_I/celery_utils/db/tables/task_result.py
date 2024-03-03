from sqlalchemy import Column, JSON, String, ForeignKey

from ._base import BaseTable


class TaskResultTable(BaseTable):
    __tablename__ = "task_result"

    task_id = Column(String, ForeignKey("task.task_id"), primary_key=True)
    result = Column(JSON)

    def __repr__(self) -> str:
        return (
            f"<TaskResult(task_id='{self.task_id}', "
            f"result(length)='{len(str(self.result))}')>"
        )
