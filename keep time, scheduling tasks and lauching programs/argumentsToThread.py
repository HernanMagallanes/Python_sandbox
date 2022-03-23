# passing arguments to the thread's target function

import threading

# print(, )

threadObj = threading.Thread(target=print,
                             args=['cats', 'dogs', 'frogs'],
                             kwargs={'sep': ' & '})

threadObj.start()

# Concurrency Issues

# multiple threads problems
# These issues happen when threads read and write variables at the same time,
# causing the threads to trip over each other.
