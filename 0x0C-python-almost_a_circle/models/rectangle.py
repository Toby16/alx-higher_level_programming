#!/usr/bin/python3
"""
class 'Rectangle'
inherited from class 'Base' in base.py
"""

from models.base import Base


class Rectangle(Base):
    """
    sub-class 'Rectangle' of class 'Base'
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        init method of class Rectangle
        Arguments:
            width: witdh of rectangle
            height: height of rectangle
            x: argument x
            y: argument y
            id: id value set to None at default
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        public getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        public setter for width
        Arguments:
            value: value assigned to 'width'
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        public getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        public setter for height
        Arguments:
            value: value assigned to 'height'
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        public getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        public setter for x
        Arguments:
            value: value assigned to 'x'
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        public getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        public setter for y
        Arguments:
            value: value assigned to 'y'
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__y = value
