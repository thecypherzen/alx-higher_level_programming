#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 4

Function(s):
    from_json_string: creates a python object from a json string
"""


def from_json_string(my_str):
    """A function that  creates an object (Python data structure)
        represented by a JSON string:


    Parameters:
        my_obj: the given object

    Returns: the JSON representation of the given object

    Notes:
        don't need to manage exceptions if the JSON string doesn't
            represent an object.
    """
    if type(my_str) is str:
        import json
        return json.loads(my_str)
