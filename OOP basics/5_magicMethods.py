# Magic/dunder methods
# Ex. representation of employees

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # dunder methods
    def __repr__(self):
        # unambiguous representation
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __str__(self):
        # readable representation
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


# Instances
emp_1 = Employee('name1', 'last1', 1000)
emp_2 = Employee('name2', 'last2', 2000)

print('')

print(emp_1)
print(repr(emp_1))
print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))

# print(emp_1 + emp_2)

# print('link of a string')
# print(len(test))
# print('test'.__len__())

# print(len(emp_1))