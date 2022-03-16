# Collatz sequence
# the simplest impossible math problem
# 3n+1 problem

# n: positive integer
# if n is even -> divide it by 2
# if n is odd -> triple it and add one
# repeat until 1

def sequence(n):
    if n != 1:

        if n % 2 == 0:
            n = int(n / 2)
            print(n)
            sequence(n)

        else:
            n = int(n * 3 + 1)
            print(n)
            sequence(n)


# validation
try:
    number = input('Enter number : \n')
    number = int(number)

    if number <= 0:
        print('only positive integer numbers')
        number = input('Enter number : ')

    # print(int(number))

except ValueError:
    print('only numbers')
    number = input('Enter number : ')

sequence(number)
