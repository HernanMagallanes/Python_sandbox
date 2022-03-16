# zigzag animation

import time
import sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 5:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
