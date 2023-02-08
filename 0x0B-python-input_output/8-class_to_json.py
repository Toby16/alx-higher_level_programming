#!/usr/bin/python3
"""
module containing function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    returns dictionary description of obj
    Arguments:
        obj
    """
    return obj.__dict__
