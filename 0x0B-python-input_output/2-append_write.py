#!/usr/bin/python3
"""
module containing function that
appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    Arguments:
        filename: name of file
        text: text to be appended
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            return file.write(text)
    except FileNotFoundError:
        with open(filename, "w", encoding="utf-8") as file:
            return file.write(text)
