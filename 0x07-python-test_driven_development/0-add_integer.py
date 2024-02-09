#!/usr/bin/python3
'''adds an integer to another'''

def add_integer(a, b=98):
    '''return the sum of a and b.
    floats are typecasted into int type
    TypeError: non integer and non.float
    '''
    if not type(int) is a and not type(float) is a:
        raise TypeError("a must be an integer or b must be a float")
    if not type(int) is b and not type(float) is b:
        raise TypeError(" must be an integer or b must be a float")
    return(int(a) + int(b))
