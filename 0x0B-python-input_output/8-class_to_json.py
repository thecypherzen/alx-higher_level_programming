#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 8

Function(s):
    class_to_json: creates a python object from json file
"""


def class_to_json(obj):
    """A function that returns the dictionary description of a class


    The class can have simple data structures (list, dictionary, string,
        integer and boolean), which are json serializable. I wish I
        understood what this meant though...the description is
        so confusing. I had to intuitively look at the examples provided
        on the intranet to deduce what's required - I hope I get it
        rightly.

    Parameters:
        obj: instance of a class

    Returns: The python object created from file

    Notes:
        must use the with statement
        need to manage exceptions if the JSON string doesn't
            represent an object.
        don't need to manage file permission exceptions.
    """
    import json
    str_data = json.dumps(obj.__dict__)
    return json.loads(str_data)
