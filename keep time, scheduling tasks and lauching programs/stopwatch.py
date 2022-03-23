# Super stopwatch
import time

# Step 1: Set up the program to track times

print('\nPress ENTER to begin.'
      ' Afterward, press ENTER to "click" the stopwatch,'
      'Press ctrl+C to quit')

input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# Step 2: Track and print lap times

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)

        lapNum_str = str(lapNum).rjust(3)
        totalTime_str = str(totalTime).rjust(5)
        lapTime_str = str(lapTime).rjust(5)

        print('Lap #%s: %s (%s)' % (lapNum_str, totalTime_str, lapTime_str), end='')

        lapNum += 1
        lastTime = time.time()

except KeyboardInterrupt:
    # handle ctrl+c
    print('\nDone')
