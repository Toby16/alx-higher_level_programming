#!/usr/bin/python3
"""
Integers addition
Module containing function to add two integers only
If arguments are not integers, error is raised
"""


def add_integer(a, b=98):
    """ a: integer argument
        b: integer argument (default value = 98)
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
