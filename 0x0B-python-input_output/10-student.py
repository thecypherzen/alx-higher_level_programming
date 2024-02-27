#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 10

Class(s):
    Student: a Student class

Notes:
    module imports not allowed
"""


class Student:
    """A class defining a student

    Attributes:
        __init__(:obj:method:puclic):  initialises the class
        to_json(:method:public): returns dictionary representation
            of the Student object
        first_name(:obj:str): student's first name
        last_name(:obj:str): student's last name
        age(:obj:int): student's age
    """
    def __init__(self, first_name, last_name, age):
        """initilises instance of Student

        Parameters:
            first_name: student's first name
            last_name: student's last name
            age: student's age
        """
        if all(isinstance(val, str) for val in [first_name, last_name])\
                and type(age) is int:
            self.first_name = first_name
            self.last_name = last_name
            self.age = age

    def to_json(self, attrs=None):
        """returns dict representation of instance of Student

        Parameters:
            attrs: list of attributes to include
                - if it's a list of strings, then only attribute names
                    in the list are to be retrieved
                - otherwise, all attributes should be retrieved

        Returns:
            the dictionary representation of a class
        """
        # if attrs is not proper, return full __dict__
        if not isinstance(attrs, list) or \
                any(not isinstance(val, str) for val in attrs):
            return self.__dict__
        # else return dict of matching keys in __dict__
        obj = {}
        for key in attrs:
            if key in self.__dict__:
                obj[key] = self.__dict__[key]
        return obj
