#!/usr/bin/python3
"""0x0C. Python - Almost a circle - Tasks 10-12, 14

This module implements incremental solutions to tasks 10 through 12
    and task 14 of this project.

Class(s):
    Square: a class defining a rectangle
"""


# Standard import
from importlib.machinery import SourceFileLoader as Loader
import os

# Local Imports
r_path = os.path.realpath("./rectangle.py")
if not os.path.exists(r_path):
    r_path = os.path.realpath("../../models/rectangle.py")
if not os.path.exists(r_path):
    r_path = os.path.realpath("models/rectangle.py")

rectangle = Loader("rectangle", r_path).load_module()
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """Defines a Square - inherits from Rectangle

    Attributes:
        __init__(method, private): class constructor
        __str__(method, private): square string constructor
        size (method, getter, setter): gets and sets `size` attribute
        to_dictionary(method, public): returns the dictionary
            representation of Square instance
        update (method, public): updates instance values
    """
    def __init__(self, size: int, x: int = 0,
                 y: int = 0, id: any = None) -> None:
        """Square class constructor

        Args:
            size: width and height of square
            x: x-axis offset
            y: y-axis offset
            id: square's id
        """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self) -> str:
        """Creates a string representation of square's instance

        Returns: string format of Rectangle class suitable for printing
            format: [Square] (<id>) <x>/<y> - <width>/<height>
        """
        rep = "[Square] " + \
            f"({self.id}) {self.x}/{self.y} - {self.size}"
        return rep

    # getters and setters
    @property
    def size(self) -> int:
        """Getter method for `size` attribute

        @setter: size(value): sets `size` to value
            - validates 'value' before assignment

        Returns: value of square's `size`
        """
        return self.width

    @size.setter
    def size(self, value: int) -> None:
        """size setter method"""
        self.width = self.height = value

    # public methods
    def to_dictionary(self):
        """returns the dictionary representation of Square
        """
        rep = {}
        keys = ["id", "size", 'x', 'y']
        for key in keys:
            rep[key] = getattr(self, key)
        return rep

    def update(self, *args: tuple, **kwargs: dict) -> None:
        """Updates Square class values

        Args:
            args: tuple of positional arguments
            kwargs: dictionary of keyword arguments

        Returns: None

        Notes:
            - if `args` is not None and not empty, `kwargs` is skipped
            - args in `args` are in the order: id, size, x, y
        """
        keys = ["id", "size", 'x', 'y']

        if args and len(args):
            length = len(args)
            max = length if length < 4 else 4
            for i in range(max):
                setattr(self, keys[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
