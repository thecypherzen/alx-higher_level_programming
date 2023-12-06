#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 9

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

    def to_json(self):
        """returns dict representation of instance of Student

        Returns:
            the dictionary representation of a class
        """
        return self.__dict__
