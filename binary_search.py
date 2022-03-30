# Binary search algorithm

import time
import random


# create a big sorted list

def sorted_list(length):
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))

    sorted_list = sorted(list(sorted_list))

    return sorted_list


# naive search:  scan entire list and ask if its equal to target

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search:  divide the list at half to find the target
# the list must be sorted !!!

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        # target > l[midpoint]:
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':

    length = 1_000
    lst = sorted_list(length)

    # Naive search
    start = time.time()

    for target in lst:
        naive_search(lst, target)
    end = time.time()
    print(f'Naive search time: {(end - start) / length} seconds')

    # Binary search
    start = time.time()

    for target in lst:
        binary_search(lst, target)
    end = time.time()
    print(f'Binary search time: {(end - start) / length} seconds')
