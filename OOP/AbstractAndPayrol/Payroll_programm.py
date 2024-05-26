# import hr
# import Employees
#
# salary_employee = Employees.SalaryEmployee(1, "John Smith", 1500)
# hourly_employee = Employees.HourlyEmployee(2, "Jane Doe", 40, 15)
# commission_employee = Employees.CommissionEmployee(3, "Kevin Bacon", 1000, 250)
#
# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(
#     [salary_employee, hourly_employee, commission_employee]
# )


import hr
import Employees
import Productivity

manager = Employees.Manager(1, "Mary Poppins", 3000)
secretary = Employees.Secretary(2, "John Smith", 1500)
sales_guy = Employees.SalesPerson(3, "Kevin Bacon", 1000, 250)
factory_worker = Employees.FactoryWorker(4, "Jane Doe", 40, 15)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
]

productivity_system = Productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)