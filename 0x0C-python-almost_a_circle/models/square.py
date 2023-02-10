#!/usr/bin/python3
"""
class 'Square'
inherited from class 'Rectangle' in rectangle.py
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    sub-sub-class 'Square' of sub-class 'Rectangle' of class 'Base'
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        class constructor
        init method of class Square
        Arguments:
            size: size of Square object
            x: argument x
            y: argument y
            id: id value set to None at default
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
