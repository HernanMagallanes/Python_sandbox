# Example of call stack of a function in Python
# Python remembers where to return the execution after each function call

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')


def b():
    print('\t b() starts')
    c()
    print('\t b() returns')


def c():
    print('\t \t c() starts')
    print('\t \t c() returns')


def d():
    print('\t c() starts')
    print('\t c() returns')


a()
