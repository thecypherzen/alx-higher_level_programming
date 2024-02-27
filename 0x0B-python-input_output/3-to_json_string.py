#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 3

Function(s):
    to_json_string: creates a JSON string representation of an object
"""


def to_json_string(my_obj):
    """A function that  creates the JSON representation of an
        object as a string:

    Doesn't check for any exceptions or permissions

    Parameters:
        my_obj: the given object

    Returns: the JSON representation of the given object

    Notes:
        don't need to manage exceptions if the object can't
            be serialized.
    """
    import json
    return json.dumps(my_obj)
