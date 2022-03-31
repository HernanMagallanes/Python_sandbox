# Time test of sorting Algorithms

import time
import timeit

import random
import threading

import sorting_algorithms as sort


def time_it(f):
    def timed(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        # t_merge = output_time(end - start)
        print(end - start)
        return result

    return timed


def output_time(time_float):
    return str(time_float)[0:5].rjust(20, '.')


if __name__ == '__main__':
    length = 10_000
    print('\nTime')

    # Bubble sort
    array = [random.randint(0, 1000) for i in range(length)]

    start = time.time()
    sort.bubble_sort(array)

    end = time.time()
    t = output_time(end - start)

    print(sort.bubble_sort.__name__)
    print(t)

    # Insertion sort
    array = [random.randint(0, 1000) for i in range(length)]

    start = time.time()
    sort.insertion_sort(array)

    end = time.time()
    t = output_time(end - start)

    print(sort.insertion_sort.__name__)
    print(t)

    # Merge sort
    array = [random.randint(0, 1000) for i in range(length)]

    start = time.time()
    sort.merge_sort(array)

    end = time.time()
    t = output_time(end - start)

    print(sort.merge_sort.__name__)
    print(t)

    # Quick sort
    array = [random.randint(0, 1000) for i in range(length)]

    start = time.time()
    sort.quick_sort(array)

    end = time.time()
    t = output_time(end - start)

    print(sort.quick_sort.__name__)
    print(t)

    # Tim sort
    array = [random.randint(0, 1000) for i in range(length)]

    start = time.time()
    sort.tim_sort(array)

    end = time.time()
    t = output_time(end - start)

    print(sort.tim_sort.__name__)
    print(t)
