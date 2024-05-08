import time
import random
import requests


def retry_on_exception(exception_type, max_retries=3, retry_interval=1):
    def decorator1(func):
        def wrapper1(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except exception_type as e:
                    retries += 1
                    time.sleep(retry_interval)
                    print(f"Retrying after {retry_interval} seconds due to {e}")
            raise RuntimeError(f"Max retries reached for {func.__qualname__}")

        return wrapper1

    return decorator1


def repeat(n):
    def decorator_with_arguments(func):
        def wrapper(*args, **kwargs):
            wrapper.calls += 1
            print(f" Function {func.__name__} has been called {wrapper.calls} times")
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        wrapper.calls = 0
        return wrapper

    return decorator_with_arguments


@retry_on_exception(ConnectionError, max_retries=3, retry_interval=1)
def get_data(url):
    return requests.get(url).json()


@retry_on_exception(exception_type=ValueError, max_retries=3, retry_interval=1)
@repeat(5)
def random_failing_function():
    if random.random() < 0.5:
        raise ValueError("Random Failure, whoho!")
    return "Success!"


result = random_failing_function()
print(result)
