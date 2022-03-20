# Getting the traceback as a string

def spam():
    bacon()


def bacon():
    raise Exception('Error message.')


spam()
