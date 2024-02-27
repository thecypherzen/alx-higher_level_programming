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
    """A function that searches and updates a file.

    If ``search_string`` is found in the file(``filename``), then
    ``new_string`` is inserted on a new line after the line where `
        `search_string`` was found.

    Parameters:
        filename(:obj:str): the name of the file to read/write from/to
        search_string(:obj:str): the string being searched for
        new_string(:obj:str): the string to insert

    Returns: None
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        max = len(lines)
        i = 0
        while i < max:
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
                i += 1
                max += 1
            i += 1
        file.seek(0)
        file.truncate(0)
        file.writelines(lines)
