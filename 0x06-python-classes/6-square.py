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
        Data:
            size (:obj: `int`): size of the square's side.
                * Defaults to 0.
                * Must be an int and must be >= 0
                * If type is not int, raises a TypeError
                * If size is < 0, raises a ValueError
            position (:obj: `tuple`): a tuple of two positive integers
                * Defaults to (0, 0)
        Methods:
            __init__: initialises the class
            area: calculates the area of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialises the square class

        Sets ``__size`` to ``size`` if ``size`` is valid
        """
        # validate size and set
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        # validate positiona and set
        if not isinstance(position, tuple) or len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0],
                          int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Is a getter of the value of __size

        Returns:
            the current value of __size
        @setter:
            sets the value of `__size` to `size` if `size` is valid
            validation is same as __init__
        """
        return self.__size

    @size.setter
    def size(self, value=None):
        """Size must be valid to set successfully

        * by default it doesn't change the already existing value
        * performs same checks on size as in __init__ before setting
        """
        if value is None:
            return
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method of the position property

        @position.setter:
            sets the square's position to `value`
            * if value is invalid, raises a TypeError

        Returns:
            position (:obj:tuple): the square's position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """value must be a tuple of 2 positive integers
                * Else, it raise a TypeError
        """
        if not isinstance(value, tuple) or len(value) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """A method of the square class - prints out the square

        Description:
            * if self.__size is 0, it prints a new line
            * Else it prints out the square using `#`
            * Preceeds the `#` with corresponding to position[0] if
                position[1] == 0 otherwise with position[1]
        """
        if not self.area():
            print("")
        else:
            # print y shift
            i = self.position[1]
            while i:
                print("")
                i -= 1
            # set height and width of square
            i = self.size
            while i:
                x = self.position[0]
                j = self.size
                while x:
                    print(" ", end="")
                    x -= 1
                while j:
                    print("#", end="")
                    j -= 1
                print("")
                i -= 1

    def area(self):
        """Calculates the area of square

        Args:
            None

        Returns:
            Area of square
        """
        return self.__size * self.__size
