#!/usr/bin/python3
"""0x0A. Python - Inheritance module - Task 1

Classes:
    MyList: inherits from ``list`` object
"""


class MyList(list):
    """A child class of the ``list`` object

    Methods:
        print_sorted: sorts a list in ascending order
    """
    def print_sorted(self):
        """A method that sorts a list in ascending order

        Returns(:obj:list): a sorted list object (self)
        """
        lcpy = self.copy()
        lcpy.sort()
        print(lcpy)
