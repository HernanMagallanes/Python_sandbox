# Property decorators - Getters, Setters and Deleters
# Ex. representation of employees

# @property
# allows us to define a method but we can access it like an attribute

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name !')
        self.first = None
        self.last = None


# Instance
emp_1 = Employee('John', 'Doe', 1000)

print('')
print(emp_1.first)
print(emp_1.last)

# Getter
print(emp_1.fullname)
print(emp_1.email)
print('')

# Setter
emp_1.fullname = 'Jack Smith'

print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)
print('')

# Deleter
del emp_1.fullname
