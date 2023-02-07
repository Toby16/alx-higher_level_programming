#!/usr/bin/python3
"""
module containing function that returns
object (Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """
    function that returns object represented by JSON
    Arguments:
        my_str: json string
    """
    return json.loads(my_str)
