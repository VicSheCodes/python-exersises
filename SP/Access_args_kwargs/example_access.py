
def example_function(*args, **kwargs):
    for arg in args:
        print(arg)
        print(type(arg))

    for key, value in kwargs.items():
        print(f"{key}: {value}")

def example_function2(*args):
    if len(args) > 1:
        second_argument = args[1]
        print("Second argument:", second_argument)
    else:
        print("There are not enough arguments.")


if __name__ == "__main__":
    example_function(1, [2, 3], 4, name="John", age=30, city="New York")
    # Example usage
    example_function2(1, 2, 3, 4, 5)
