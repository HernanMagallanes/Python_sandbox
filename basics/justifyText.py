# Strings

# Operators : in , not in > True / False
# String methods : upper() , lower() & isupper() , islower()
# isX() methods : isalpha() , isalnum() , isdecimal() , isspace() , istitle()
# -> True / False
# startswith() , endswith()
# join() , split() (str -> list) & partition()
# remove white spaces : strip(), rstrip() , lstrip()
# numeric vales  : ord() , chr()
# Justify text ; rjust() , ljust() , center()

# import sys
# print(sys.version)

s = 'Hello world'


def text(s, n):
    r = s.rjust(n, '-')
    c = s.center(n, '-')
    l = s.ljust(n, '-')

    print(r)
    print(c)
    print(l)


text(s, 40)
