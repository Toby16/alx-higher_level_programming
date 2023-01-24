#!/usr/bin/python3
"""
class 'Square' that defines a square
"""


class Square:
    """
    Defines a square
    Attributes:
        size: size of square
    """
    def __init__(self, size=0):
        """
        init method of class 'Square'
        Args:
            size: size of square
        """
        self.__size = size
        if not (isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        else:
            if self.__size < 0:
                raise ValueError("size must be >= 0")

    @property
    def size(self):
        """
        method to retrieve 'size'

        Returns:
            self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        method to set value to size
        Args:
            value
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must me >= 0")
            else:
                self.__size = value

    def area(self):
        """
        method to return current square area

        Return:
            size ** 2
        """
        return (self.__size ** 2)
