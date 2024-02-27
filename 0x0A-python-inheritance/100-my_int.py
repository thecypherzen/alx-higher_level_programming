#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 12

Classes:
    MyInt: Inherits from int
"""


class MyInt(int):
    """A Rebel int subclass"""
    def __eq__(self, b):
        """Does the reverse of the `==` logic sign"""
        return not int.__eq__(self, b)

    def __ne__(self, b):
        """Does the reverse of != logic sign"""
        return not int.__ne__(self, b)
