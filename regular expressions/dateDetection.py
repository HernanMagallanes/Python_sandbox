# date detection
# DD/MM/YYYY format
# years range from 1000 to 2999
# day or month with leading zero (0n)
# date validation

import re


def date_detection():
    string = str(input('Ingress date: '))

    dateRegex = re.compile(r'(^[0-3]\d)/([0-1]\d)/([1-2]\d{3})')

    mo = dateRegex.search(string)
    day, month, year = mo.groups()

    # date validation

    # 04 Apr / 06 June / 09 Sep / 11 Nov -> 30 days
    if month == '04' or month == '06' or month == '09' or month == '11':
        if day == '31':
            print('Invalid date')

    # 02 Feb -> 28 days
    if month == '02':
        if day == '30' or day == '31':
            print('Invalid date')

        # leap year : 02 Feb -> 29 days
        year_int = int(year)

        if day == '29':
            if year_int % 4 != 0 and (year_int % 400 == 0 or year_int % 100 != 0):
                print('Invalid date')

    print(f'\n day: {day} month: {month} year: {year}')


date_detection()
