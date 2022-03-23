# reference: January 1, 1970
# unit: seconds
# time.time()

import time


def calc_prod():
    product = 1
    for i in range(1, 100_000):
        product *= i

    return product


startTime = time.time()
prod = calc_prod()
endTime = time.time()

print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

# current time , human-readable
# print(time.ctime())
