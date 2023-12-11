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
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor

        Args:
            size (`int`): width and height of square
            x (`int`): x-axis offset
            y (`int`): y-axis offset
            id (`any`): square's id
        """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """Creates a string representation of square's instance

        Returns: string format of Rectangle class suitable for printing
            format: [Square] (<id>) <x>/<y> - <width>/<height>
        """
        rep = "[Square] " + \
            f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return rep


s = Square(3)
s.update(height=2)
print(s.height)
