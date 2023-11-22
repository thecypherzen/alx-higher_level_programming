#!/usr/bin/python3
"""Creation and usage of a square

A module that creates a square class

Classes:
    Square: the square class

Description:
    No module imports allowed
"""


class Square():
    """A class that defines a square

    Attributes:
        __init__: initialises the class
        size (:obj: `int`): size of the square's side.
            * Defaults to 0.
            * Must be an int and must be >= 0
            * If type is not int, raises a TypeError
            * If size is < 0, raises a ValueError
        area: calculates the area of square
    """
    def __init__(self, size=0):
        """Initialises the square class

        Sets ``__size`` to ``size`` if ``size`` is valid
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of square

        Args:
            None

        Returns:
            Area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Is a getter of the value of __size

        Returns:
            the current value of __size
        """
        return self.__size

    @size.setter
    def size(self, value=None):
        """Size must be valid to set successfully

        * by default it doesn't change the already existing value
        * performs same checks on size as in __init__ befor setting
        """
        if value is None:
            return
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """A method of the square class - prints out the square

        Description:
            * if self.__size is 0, it prints a new line
            * Else it prints out the square using `#`
        """
        if not self.area():
            print("")
        else:
            i = self.size
            while i > 0:
                j = self.size
                while j:
                    print("#", end="")
                    j -= 1
                print("")
                i -= 1
