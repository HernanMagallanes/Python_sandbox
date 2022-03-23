# Multithreading
# Python programs by default have a single thread of execution.

import threading
import time

print('Start of program.')


def nap():
    time.sleep(5)
    print('Wake up!')


# function as a argument, not call it
threadObj = threading.Thread(target=nap)

threadObj.start()

print('End of program.')
