#!/usr/bin/python3
"""0x0C. Python - Almost a circle - Task 1, 15-19

Class(s):
    Base: project's base/super class
        to be inherited by subsequent classes
"""


import json


class Base:
    """Project's base class

    Attributes:
        __nb_objects(int, private): number of class instances
        __init__(method, private): instance init method
        to_json_string(method, public): json_stringifyer of list
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises a class object

        If id is None, sets instance id to objects_count+1, else
            sets it to the passed value.
            - does not check for type conformance to int so passing non-ints
                may cause unexpected behaviour

        Parameters:
            id(:obj:int): instance's id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries:list) -> str:
        """creates json_string representation of Square

        Args:
            list_dictionaries: list of dictionaries to
                stringify

        Returns: json_string form of `list_dictionaries`.
        """
        if not list_dictionaries or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)


