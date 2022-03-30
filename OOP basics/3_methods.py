# Class methods and static methods
# Ex. representation of employees

# class methods - take the class as the first argument
# static methods - don't pass anything behave like regular functions
# logical connection with the class


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    # regular method
    # take the instance as the instance as first argument
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # class methods as alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')

        # new employee object
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    pass


# Instances
emp_1 = Employee('name1', 'last1', 1000)
emp_2 = Employee('name2', 'last2', 2000)

print(emp_1.raise_amount)
emp_1.set_raise_amt(1.05)
print(emp_1.raise_amount)
print('')

# class methods as alternative constructor
# specific case: data as string
emp_3_str = 'John-Doe-3000'

#  without the class method
# first, last, pay = emp_3_str.split('-')
# emp_3 = Employee(first, last, pay)

emp_3 = Employee.from_string(emp_3_str)
print(emp_3.email)
print(emp_3.pay)
print('')

# static method example

import datetime

my_date = datetime.date(2022, 3, 29)

print('workday ?')
print(Employee.is_workday(my_date))
