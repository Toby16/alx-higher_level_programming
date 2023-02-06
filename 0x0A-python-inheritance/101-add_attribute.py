#!/usr/bin/python3
"""
Module containing:
function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr, val):
    """
    method to add attribute to object if possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, val)
