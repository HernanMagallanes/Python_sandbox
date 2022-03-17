# Regex version of the strip() method

# no args remove whitespace from the beginning and the end
# 2nd arg remove from the str

import re


def regex_strip(string_expr, *string_delete):
    # print('\n')
    # print(str_expr)

    passwordRegex = re.compile(r'([\w\d].*)')
    mo = passwordRegex.search(str(string_expr))
    print(mo.group())

    if string_delete:
        print(f'\n delete : {string_delete}')
        passwordRegex = re.compile(r'(string_delete).*')
        mo = passwordRegex.search(str(string_expr))
        print(mo)

        # delete with regex

    pass


regex_strip('        helloworld      ', 'world')
