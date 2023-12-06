#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 2

Function(s):
    append_write: appends content to a file
"""


def append_write(filename="", text=""):
    """A function that appends a string to end of a UTF8 text file

    Doesn't check for any exceptions or permissions

    Parameters:
        filename(:obj:str): the name of file to write to
        text(:obj:str): string to write to file

    Returns: the number of characters written

    Notes:
        Must use with statement
        Create file if not exists
        Overwrite file if it exists
        Module imports not allowed
    """
    if type(filename) is str:
        with open(filename, mode="a", encoding='utf-8') as ifile:
            res = ifile.write(text)
            return res
