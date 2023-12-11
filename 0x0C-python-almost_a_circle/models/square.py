#!/usr/bin/python3
"""0x0C. Python - Almost a circle - Tasks 10-12, 14

This module implements incremental solutions to tasks 10 through 12
    and task 14 of this project.

Class(s):
    Square: a class defining a rectangle
"""


# Local Imports
from rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square - inherits from Rectangle

    Attributes:
        __init__(method, private): class constructor
        __str__(method, private): square string constructor
        size:(method, getter, setter): gets and sets `size` attribute
    """
    def __init__(self, size:int, x:int=0, y:int=0, id:any=None) -> None:
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
            f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return rep

    @property
    def size(self) -> int:
        """Getter method for `size` attribute

        @setter: size(value): sets `size` to value
            - validates 'value' before assignment

        Returns: value of square's `size`
        """
        return self.width

    @size.setter
    def size(self, value:int) -> None:
        self.width = self.height = value
