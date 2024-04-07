import time

def retry_on_exception(exception_type, max_retries=3, delay_seconds=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except exception_type as e:
                    print(f"Retrying after {delay_seconds} seconds due to {e.__class__.__name__}: {e}")
                    time.sleep(delay_seconds)
                    retries += 1
            raise RuntimeError(f"Max retries reached. Unable to complete operation after {max_retries} attempts.")

        return wrapper

    return decorator

# Example usage:

@retry_on_exception(exception_type=ValueError, max_retries=3, delay_seconds=2)
def possibly_failing_function():
    import random
    if random.random() < 0.8:
        raise ValueError("Random failure")
    return "Success!"

result = possibly_failing_function()
print(result)
