#!/usr/bin/python3
"""
module containing function that reads a text file
and prints it out to stdout
"""


def read_file(filename=""):
    """
    function that reads text file and prints it
    Arguments:
        filename: name of file
    """
    with open(filename, "r", encoding="utf-8") as file:
        """
        open file
        read content of file
        close file safely
        """
        print(file.read())
