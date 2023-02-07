#!/usr/bin/python3
"""
Module containing function that writes a string to a text file"
"""


def write_file(filename="", text=""):
    """
    function that writes string to text file
    Arguments:
        filename: name of file
        text: string to be written in text file
    Returns: number of string written into text file
    """
    with open(filename, "w", encoding="utf-8") as file:
        """
        open file of name 'filename'
        """
        x = file.write(text)
    return x
