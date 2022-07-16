from hr import Hourly, Salaried, Commission
from contacts import Address


class PayrollSystem:
    def __init__(self) -> None:
        pass

    def calculate_payroll(self, employees) -> None:
        for employee in employees:
            employee.calculate_payroll()


hourly_employee = Hourly(1, "John Smith", 50, 40)

# This is compostion. Instance of Address class is used as a variable in Employee class
hourly_employee.address = Address("123 main street", "SomeCity", "CO", "12345")

salaried_employee = Salaried(2, "Jane Smith", 1200)
commission_employee = Commission(3, "Foo Bar", 1200, 30)

employees = [hourly_employee, salaried_employee, commission_employee]

p = PayrollSystem()
p.calculate_payroll(employees)
