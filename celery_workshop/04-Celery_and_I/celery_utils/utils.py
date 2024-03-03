import time
from typing import Any, Callable, Optional


class TimeoutException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


def _default_failure_func() -> None:
    raise TimeoutException("Timeout at wait_until")


def wait_until(
    condition: Callable[[], bool],
    success_func: Callable[[], Any],
    failure_func: Callable[[], Any] = _default_failure_func,
    timeout: Optional[float] = None,
    interval: float = 0.5,
) -> Any:
    start_time = time.time()
    while (start_time + timeout) > time.time() if timeout else True:
        if condition():
            return success_func()

        time.sleep(interval)
    failure_func()
