#!/usr/python3
"""
Integers addition
"""

from math import floor

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
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    return a + b
