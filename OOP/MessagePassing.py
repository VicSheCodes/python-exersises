"""
Sending a message: This refers to the act of calling a method on an object. When you send a message to an object,
you're requesting it to perform some action or computation by invoking one of its methods.

Passing parameters: Parameters are values that are provided to a method when it's called.
They represent the data or information necessary for the method to perform its task.
When you send a message with parameters to an object,
you're providing input data that the object's method will operate on.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."


# Creating an instance of Person
john = Person("John")
mapping_proxy_1 = Person.__dict__
mapping_proxy_2 = john.__dict__
print(mapping_proxy_1 == mapping_proxy_2)  # Output: False
print(f"\n {mapping_proxy_1 =}\n")
print(f"\n {mapping_proxy_2 =}\n")

# Sending a message to the john object

greeting = john.greet()
print(greeting)  # Output: Hello, my name is John.
