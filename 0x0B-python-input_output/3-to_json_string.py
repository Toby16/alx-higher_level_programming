#!/usr/bin/python3
"""
module containing function to
return the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
    function to return JSON representation
    Arguments:
        my_obj: objected to be represented
    """
    return json.dumps(my_obj)
