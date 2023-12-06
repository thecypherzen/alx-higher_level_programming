#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 5

Function(s):
    save_to_json_file: writes an object to a file as json
"""


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
        using a JSON representation


    Parameters:
        my_obj: the given object
        filename: name of file to write json string to

    Returns: None

    Notes:
        don't need to manage exceptions if the object can't
            be serialized.
        don't need to manage file permission exceptions.
    """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file, indent=4)
