# Simple countdown program

import subprocess
import time


# Step 1 : Count down

def count_down(time_left=5):
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left -= 1

    # Step 2 : Play the sound file
    # alarm.wav at the same directory

    subprocess.Popen(['start', 'alarm.wav'], shell=True)
    raise Exception('file.wav not found.')


try:

    count_down(5)
except Exception as err:
    print('An exception happened: ' + str(err))
