def my_decorator_with_args(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix}: Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print(f"{prefix}: Something is happening after the function is called.")
            return result
        return wrapper
    return decorator


@my_decorator_with_args("LOG")
def say_hello(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    say_hello("Alice")
