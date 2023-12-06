#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 6

Function(s):
    load_from_json_file: creates a python object from json file
"""


def load_from_json_file(filename):
    """A function creates a python object from a json file


    Parameters:
        filename: name of file to read from

    Returns: The python object created from file

    Notes:
        must use the with statement
        need to manage exceptions if the JSON string doesn't
            represent an object.
        don't need to manage file permission exceptions.
    """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
