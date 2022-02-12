"""
Class methods vs Static methods

Static methods doesn't require self or other methods, It is completely solo method

Class method is used to work with instance or to create a instance and it can access other methods

"""
import datetime


class Employee:
    increment = 15

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self, year):
        salary = self.salary
        for _ in range(1, year+1):
            salary = salary + salary * (self.increment / 100)
        return salary

    @classmethod
    def raise_increment(cls, percentage):
        cls.increment = percentage

    @classmethod
    def from_string(cls, string):
        name, salary = string.split('-')
        return cls(name, salary)

    def __str__(self):
        return f"{self.name} getting {self.salary} Salary!!!"

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Prabhu", 10000)
emp2 = Employee("Rabiya", 15000)
emp3 = Employee("Dhibakar", 20000)

emp4 = Employee.from_string('John-50000')
print(emp1)
print(emp4)


myDate = datetime.date(2021, 7, 24)
print(Employee.is_workday(myDate))
