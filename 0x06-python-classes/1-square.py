#!/usr/bin/python3
class Square():
    """A class that defines a square.

    Attriubutes:
        __size (:obj: `int`): size of the square's side

    """

    def __init__(self, size):
        """Square class initialization"""
        self.__size = size


mysquare = Square(3)
print(mysquare.__doc__)
print(mysquare.__init__.__doc__)