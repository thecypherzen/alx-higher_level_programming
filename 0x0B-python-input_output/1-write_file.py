#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 1

Function(s):
    write_file: writes content to a file
"""


def write_file(filename="", text=""):
    """A function that writes a string to a UTF8 text file

    Doesn't check for any exceptions or permissions

    Parameters:
        filename(:obj:str): the name of file to write to
        text(:obj:str): string to write to file

    Returns: the number of characters written

    Notes:
        Must use with statement
        Create file if not exists
        Overwrite file if it exists
    """
    if type(filename) is str:
        with open(filename, mode="w", encoding='utf-8') as ifile:
            res = ifile.write(text)
            return res
