# date arithmetic on datetime values

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)

print(f'\n{dt + thousandDays}')

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)

print(f'\n{oct21st - aboutThirtyYears}')
print(f'\n{oct21st - 2 * aboutThirtyYears}')
