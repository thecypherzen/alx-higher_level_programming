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

    @staticmethod
    def from_json_string(json_string:json) -> list:
        """converts a json string to a list

        Args:
            json_string: a string representing a list of dictionaries

        Returns: list from json_string

        Notes:
            If json_string is None or empty, return an empty list,
                otherwise, return the list represented by json_string
        """
        if not json_string or type(json_string) is not str or \
            not len(json_string):
            return []
        return json.loads(json_string)


    @staticmethod
    def to_json_string(list_dictionaries:list) -> json:
        """creates json_string representation of Square

        Args:
            list_dictionaries: list of dictionaries to
                stringify

        Returns: json_string form of `list_dictionaries`.
        """
        if not list_dictionaries or \
            type(list_dictionaries) is not list or \
                not len(list_dictionaries):
            return json.dumps([])
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs:list) -> None:
        """saves a jsonifyed list to a given file

        It writes the JSON string reps of `list_objs`
            to a file:

        Args:
            list_objs: a list of instances that inherit
                from Base - eg: list of Rectangle instances or
                list of Square instances

        Returns: None

        Notes:
            - If list_objs is None, an empty list is saved
            - The filename must be: <Class name>.json
                - example: Rectangle.json
            - must use the static method to_json_string
                (created before)
            - must overwrite the file if it already exists
        """
        f_obj = []
        # add objs to list if of valid type
        if list_objs and type(list_objs) is list and \
            len(list_objs):
            for obj in list_objs:
                f_obj.append(obj.to_dictionary())

        # jsonify list and write to file
        f_str = cls.to_json_string(f_obj)
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(f_str)
