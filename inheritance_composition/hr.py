from abc import ABC, abstractmethod

# Make this an abstract class because this class is only meant to be extended
# Decorate calculate_payroll method as abstract because whoever extends this class must implement it
class Employee(ABC):
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.address = None

    @abstractmethod
    def calculate_payroll(self):
        pass


class Salaried(Employee):
    def __init__(self, id, name, weekly_salary) -> None:
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class Hourly(Employee):
    def __init__(self, id, name, rate, hours_worked) -> None:
        super().__init__(id, name)
        self.rate = rate
        self.hours_worked = hours_worked

    def calculate_payroll(self):
        return self.hours_worked * self.rate


class Commission(Salaried):
    def __init__(self, id, name, weekly_salary, commission) -> None:
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        # Use calculate_payroll method from base class (Salaried) because if the defintion changes, the logic is centralized
        return super().calculate_payroll() + self.commission
