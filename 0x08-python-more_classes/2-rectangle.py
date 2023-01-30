#!/usr/bin/python3
"""
Area and Perimeter
class 'Rectangle' that defines a rectangle
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
        init method of class 'Rectangle'
        Arguments:
            width
            height
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height

    @property
    def width(self):
        """
        method to retrieve self.width
        Args:
            No arguments besides 'self'
        Return:
            self.width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        method to assign 'value' to 'self.width'
        Args:
            value
        """
        if not isinstance(value, int):
            """
            if value is not of type 'int'
                TypeError is raised
            """
            raise TypeError("width must be an integer")
        elif value < 0:
            """
            if value is less than 0
                ValueError is raised
            """
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        method to retrieve self.height
        Args:
            No arguments besides 'self'
        Return:
            self.height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        method to assign 'value' to 'self.height'
        Args:
            value
        """
        if not isinstance(value, int):
            """
            if value is not of type 'int'
                TypeError is raised
            """
            raise TypeError("height must be an integer")
        elif value < 0:
            """
            if value is less than 0
                valueError is raised
            """
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


    def area(self):
        """
        method that returns area of the rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        method to return perimeter of the rectangke
        """
        if (self.width == 0) or (self.height == 0):
            """
            if width or height equals 0
                0 is returned
            """
            return 0
        else:
            return (2 * (self.height + self.width))
