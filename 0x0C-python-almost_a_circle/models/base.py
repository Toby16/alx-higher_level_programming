#!/usr/bin/python3
"""
Module containing the Base class
"""

import json


class Base:
    """
    'Base' class
    This class is the 'base' of all other classes in this project
    The goal is to manage 'id' attribute in all future classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method of class 'Base'
        Arguments:
            id: default value set to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns
            JSON representation of 'list_dictionaries'
        Arguments:
            list_dictionaries: a list of dictionaries

        Returns: [], if list_dictionaries is None or empty
                else, JSON string representation of 'list_dictionaries'
        """
        if (len(list_dictionaries) == 0) or (list_dictionaries is None):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
