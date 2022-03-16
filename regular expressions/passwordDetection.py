# strong password detection

# at least ...
# 8 characters long
# 1 uppercase
# 1 lowercase
# 1 digit

import re


def password():
    string = str(input('Ingress password: '))

    passwordRegex = re.compile(r'''
                ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)
                [a-zA-Z\d]{8,}
                ''', re.VERBOSE)

    mo = passwordRegex.fullmatch(string)

    if not mo:
        print('weak password')
    else:
        print('strong password')


password()
