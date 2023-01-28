#!/usr/python3
"""
Integers addition
"""


def add_integer(a, b=98):
    """
    method of '0-add_integer module'
    Args:
        a: integer argument
        b: integer argument (default value = 98)
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(round(a, 0))
    if isinstance(b, float):
        b = int(round(b, 0))
    
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.txt")
