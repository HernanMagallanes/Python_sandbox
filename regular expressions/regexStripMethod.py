# Regex version of the strip() method
# no args -> remove whitespace from the beginning and the end
# 2nd arg ->  remove from the str

import re


def regex_strip(string_expr, string_delete=''):

    string_regex = re.compile(r'([\w\d].*)')
    mo = string_regex.search(str(string_expr))
    str_strip = mo.group()

    print(f"\nstring : \n'{string_expr}' ")
    print(f"\nstrip string: \n{str_strip}")

    if string_delete != '':

        ''' 
        # remove with list
        aux = string_expr.split()
        string_list_comp = [s for s in aux if s != string_delete]
        print(string_list_comp)
        '''

        # remove with regex
        string_regex = re.compile(rf'({string_delete})')
        new_mo = string_regex.search(str_strip)

        try:
            if new_mo:
                str_clean = re.sub(rf'({string_delete})', '', str_strip)
            else:
                raise Exception('word NOT found')

            print(f"\nclean string: \n{str_clean}")

        except Exception as err:
            print('\nAn exception happened: ' + str(err))


regex_strip('   hello world      ', 'hello')
