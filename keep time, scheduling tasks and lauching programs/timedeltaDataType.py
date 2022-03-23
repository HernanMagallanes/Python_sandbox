# timedelta data type
# represents duration rather than a moment in time

import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

print(f'\ndays: {delta.days} \tseconds: {delta.seconds} \tmicroseconds, {delta.microseconds}')

print(f'total seconds: {delta.total_seconds()}')

print(f'delta: {str(delta)}')
