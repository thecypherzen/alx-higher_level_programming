#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 0

Function(s):
    read_file: reads and prints a file's content
"""


def read_file(filename=""):
    """A function that reads and prints a file's content

    Doesn't check for any exceptions or permissions

    Parameters:
        filename(:obj:str): the name of file to read

    Returns: None
    """
    if type(filename) is str:
        with open(filename, mode="r", encoding='utf-8') as ifile:
            for line in ifile.readlines():
                print(line)
