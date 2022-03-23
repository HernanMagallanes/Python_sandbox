import datetime
import time

print(datetime.datetime.now())

dt = datetime.datetime(2019, 10, 21, 16, 29, 0)

print(f'year: {dt.year} \t month: {dt.month} \t day: {dt.day}')
print(f'hour: {dt.hour} \t minute: {dt.minute} \t second: {dt.second}')

print('\ntime stamp 0f 1000000:')
print(datetime.datetime.fromtimestamp(1_000_000))

print('\ntime stamp of now:')
print(datetime.datetime.fromtimestamp(time.time()))
