# Classes and instances
# Ex. representation of employees

class Employee:
    # instance variables
    # constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    # method
    def fullname(self):
        return f'{self.first} {self.last}'


# Instances
emp_1 = Employee('name1', 'last1', 1000)
emp_2 = Employee('name2', 'last2', 2000)

print('\nemail:')
print(emp_1.email)
print(emp_2.email)

print('\nfullname:')
print(emp_1.fullname())
print(emp_2.fullname())

print('\nclass dict')
print(emp_1.__dict__)