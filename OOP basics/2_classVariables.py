# Class variables - shared among all instance
# Ex. representation of employees

class Employee:
    # class variable
    raise_amount = 1.04
    num_of_emps = 0

    # constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    # method
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Instances
emp_1 = Employee('name1', 'last1', 1000)
emp_2 = Employee('name2', 'last2', 2000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print('')
print(emp_1.raise_amount)
emp_1.raise_amount = 1.05
print(emp_1.raise_amount)

print('\nclass variables\n')
print(Employee.__dict__)
print('\n')
print(emp_1.__dict__)

print('\nnum of employees:')
print(Employee.num_of_emps)
