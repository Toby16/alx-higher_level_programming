#!/usr/bin/python3
"""
Module containing the Base class
"""


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
