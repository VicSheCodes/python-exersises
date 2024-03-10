import time
'''
In this example, my_decorator is a simple decorator that wraps the say_hello function. 
When say_hello is called, it is actually wrapper that gets executed, allowing us to add 
functionality before and after the original function call.
'''

def basic_decorator(func):
    def wrapper():
        print(f" Some actions before the {func.__qualname__} called.")
        func()
        print(f" Some actions after the {func.__qualname__} called.")
    return wrapper

@basic_decorator
def say_hello():
    print(" Hello, World!")

def repeat(n):
    def decorator_with_arguments(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_with_arguments

names = ["Aaron", "Bob", "Charlie"]
@repeat(3)
def say_hello_again(names):
    for name in names:
        print(f" Hello, {name}!")

class ClassBasedDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        print(f" \n Some actions before the {self.func.__qualname__} called.")
        self.func(*args, **kwargs)
        print(f" Some actions after the {self.func.__qualname__} called.")
        end_time = time.time() - start_time
        print(f" The {self.func.__qualname__} took {end_time:.5f} seconds to run")

@ClassBasedDecorator
def say_my_name(name):
    time.sleep(1)
    print(f" Hello, {name}!")

def exclamation_decorator(func):
    def wrapper(*args, **kwrgs):
        result = func(*args, **kwrgs)
        return f"{result}!"
    return wrapper

def question_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}?"
    return wrapper

@exclamation_decorator
@question_decorator
def punctuation1(name):
    return name


@question_decorator
@exclamation_decorator
@exclamation_decorator
def punctuation2(name):
    return name

def counter_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} has been called {wrapper.calls} times.")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper
@counter_decorator
def what_time_is_it():
    start_time = time.time()
    time.sleep(1)
    print(f"{time.strftime('%H:%M:%S', time.localtime(start_time))}")


def memoize(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class Config:
    _instance = None

    def __init__(self, config_data):
        self.config_data = config_data

    @classmethod
    def get_instance(cls, config_data):
        if cls._instance is None:
            cls._instance = cls(config_data)
        return cls._instance

# Using the class method to get the singleton instance
config_instance = Config.get_instance({"key": "value"})


if __name__ == "__main__":
    # say_hello()
    # say_hello_again(names)
    # say_my_name("Victoria")
    # print(punctuation1("Victor"))
    # print(punctuation2("Victor"))
    what_time_is_it()
    what_time_is_it()
    result = fibonacci(10)
    print(result)

