# Assertions
# "I assert that th condition holds true, and if not,
# there is a bug somewhere, so immediately stop the program"

ages = [26, 57, 92, 54, 22, 15, 17, 80, 73]

# case 1
# ages.sort()

# case 2
ages.reverse()

print(ages)

# sanity check
# True -> do nothing
assert ages[0] <= ages[-1]

# with assert fails the program should crash.
# assertions are for programmer errors, not user errors.
# only fail in development.
# raising exceptions for user error
