import random


class SayHello():
    def __init__(self, name='Vic'):
        self.name = name

    random_number = random.randint(1, 100)

    def say_hello(self):
        print(f" Hello, {self.name}!")

    @classmethod
    def say_hello_again(cls):
        print(f" Hello, {cls.random_number} times!")


if __name__ == '__main__':
    say_hello = SayHello(name='Sweetty')
    say_hello.say_hello()

    SayHello.say_hello_again()


class Employee:
    next_id = 1

    def __init__(self, name, salary):
        self.id = Employee.next_id
        Employee.next_id += 1
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Salary: ${self.salary}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Company:
    employees = []

    @staticmethod
    def add_employee(employee):
        Company.employees.append(employee)

    @classmethod
    def display_employees(cls):
        for emp in cls.employees:
            emp.display()


# Create employees
dev1 = Developer("Alice", 60000, "Python")
dev2 = Developer("Bob", 65000, "Java")
manager1 = Manager("Charlie", 80000, "Engineering")

# Add employees to the company
Company.add_employee(dev1)
Company.add_employee(dev2)
Company.add_employee(manager1)

# Display all employees in the company
Company.display_employees()
