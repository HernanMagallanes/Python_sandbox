# Logging
# create custom messages and display with log

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asc_time)s - %(level_name)s - %(message)s')

# disable log messages
logging.disable(logging.CRITICAL)


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))

    total = 1
    for i in range(1, n + 1):
        total *= i

        logging.debug('i is ' + str(i) + ', total is ' + str(total))

    logging.debug('End of factorial(%s)' % (n))

    return total


print(factorial(5))
logging.debug('End of program')

'''
    Logging levels

DEBUG - logging.debug()
INFO - logging.info()
WARNING - logging.warning()
ERROR - logging.error()
CRITICAL  - logging.debug()

    Logging to a file

logging.basicConfig(
    filename='myProgramLog.txt',
    level=logging.DEBUG,
    format=' %(asc_time)s - %(level_name)s - %(message)s')

'''
