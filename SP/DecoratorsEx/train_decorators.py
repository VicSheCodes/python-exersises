from functools import wraps


def exclamation_decorator(func):
    # Initialize the counter
    counter = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter  # Use nonlocal to access the counter variable
        counter += 1  # Increment the counter
        res = func(*args, **kwargs)
        return f"{res}!"

    # Add an attribute to the wrapper function to access the counter
    wrapper.execution_count = lambda: counter

    return wrapper


# Example usage
@exclamation_decorator
def say_hello(name):
    return f"Hello, {name}"


# Call the decorated function
print(say_hello("Alice"))  # Output: Hello, Alice!
print(say_hello("Bob"))    # Output: Hello, Bob!

# Access the execution count attribute
print("Execution count:", say_hello.execution_count())  # Output: 2
