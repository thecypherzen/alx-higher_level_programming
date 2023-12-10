#!/usr/bin/python3
"""0x0C. Python - Almost a circle - Task 1

Class(s):
    Base: project's base/super class
        to be inherited by subsequent classes
"""


class Base:
    """Project's base class

    Attributes:
        __nb_objects(:obj:int): number of class instances
        __init__(:obj:method): instance init method
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
	