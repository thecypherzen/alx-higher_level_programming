#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 13(advanced)

Function(s):
    append_after: inserts a line after the line containing a
        certain string

Notes:
    module imports not allowed
    must use the with statement
    don’t need to manage file permission or file doesn't exist
        exceptions.
"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line in a file

    The value is inserted after the line that contains a given string.

    Parameters:
        filename(:obj:str): the name of the file to read/write from/to
        search_string(:obj:str): the string being searched for
        new_string(:obj:str): the string to insert

    Returns: None
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        for line in lines:
            if search_string in line:
                if line[-1] != '\n':
                    new_string = "\n" + new_string
                lines.insert(lines.index(line) + 1, new_string)
        file.seek(0)
        file.truncate(0)
        file.writelines(lines)
