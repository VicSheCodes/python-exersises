from abc import ABC, abstractmethod


# abstract base class, exist to be inherited, but never instantiated
class _Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"\n Employee({self.name=}, {self.salary=})"

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(_Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(_Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

    def __repr__(self):
        return f"\n HourlyEmployee({self.name=}, {self.hours_worked=}, {self.hourly_rate=})"


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        return fixed_salary + self.commission

    def __repr__(self):
        return f"\n CommissionEmployee({self.name=}, {self.weekly_salary=}, {self.commission=})"


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} screams and yells for {hours} hours.")


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing office paperwork.")


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours on the phone.")


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"{self.name} manufactures gadgets for {hours} hours.")
