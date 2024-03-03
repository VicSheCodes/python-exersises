from enum import Enum


class Status(Enum):
    # 1 <= code < 100 = Creation State - Pre run
    PENDING = 0
    CREATED = 1
    # 100 <= code < 200 = Running statuses
    STARTED = 100
    # 200 <= code < 300 = Completed successfully
    SUCCESS = 200
    # 300 <= code < 400 = Completed with Failure
    FAILED = 300


completed_statuses = [Status.SUCCESS, Status.FAILED]


def is_completed(status: Status) -> bool:
    return status in completed_statuses
