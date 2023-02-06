#!/usr/bin/python3
"""
class "MyInt" that inherits from "int"
"""


class MyInt(int):
    """
    class MyInt
    """
    def __init__(self, value):
        """
        init method for class MyInt
        """
        self.value = value

    def __eq__(self, num):
        return (self.value != num)

    def __ne__(self, num):
        return (self.value == num)

    def __str__(self):
        return str(self.value)
