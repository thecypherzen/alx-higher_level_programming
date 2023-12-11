#!/usr/bin/python3
"""0x0C. Python - Almost a circle - Tasks 2-9, 13

This module implements incremental solutions to tasks 2 through 9
of this project.

Class(s):
    Rectange: a class defining a rectangle
"""


# Local imports
import validators
from base import Base


class Rectangle(Base):
    """Defines a rectangle - inherits from Base

    Attributes:
        __init__(method, private): class constructor
        __str__(method, magic): returns string format of rectangle
        area(method, public): returns the area of rectangle instance
        display(method, public): renders rectangle intance with
            the char '#'
        height (:obj: `getter`, `setter`): getter/setter of height
        to_dictionary(method, public): returns the dictionary representation
            of Rectangle instance.
        update(method, public): update's instance values
        width (:obj: `getter`, `setter`): getter/setter of width
        x (:obj: `getter`, `setter`): getter/setter of property x
        y (:obj: `getter`, `setter`): getter/setter of property y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises instance of rectangle

        Args:
            width (`int`): rectangle's width, must be > 0
            height (`int`): rectangle's height, must be > 0
            x (`int`, optional): position on x axis,
                must be >= 0
            y (`int`, optional): position on y axis,
                must be >= 0
            id (`any`, optional): instance's id number
        """
        validators.gt_zero_validate(width, "width", typ="int")
        validators.gt_zero_validate(height, "height", typ="int")
        validators.pos_num_validate(x, 'x', typ="int")
        validators.pos_num_validate(y, 'y', typ="int")
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # private attribute setters
    @property
    def width(self) -> int:
        """:obj `int`: Getter of width property

        Setter Args:
            value(`int`): update value of `width` to `value`
        """
        return self.__width

    @property
    def height(self) -> int:
        """:obj: `int`: Getter of height property

        Setter Args:
            value(`int`): update value of `height` to `value`
        """
        return self.__height

    @property
    def x(self) -> any:
        """:obj: `any`: Getter of x property

        Setter Args:
            value(`any`): update value of `x` to `value`
        """
        return self.__x

    @property
    def y(self) -> any:
        """:obj: `any`: Getter of y property

        Setter Args:
            value(`any`): update value of`y` to `value`
        """
        return self.__y

    # private attribute setters
    @width.setter
    def width(self, value) -> None:
        """width setter method"""
        validators.gt_zero_validate(value, "width", typ="int")
        self.__width = value

    @height.setter
    def height(self, value) -> None:
        """height setter method"""
        validators.gt_zero_validate(value, "height", typ="int")
        self.__height = value

    @x.setter
    def x(self, value) -> None:
        """x setter method"""
        validators.pos_num_validate(value, 'x', typ="int")
        self.__x = value

    @y.setter
    def y(self, value) -> None:
        """y setter method"""
        validators.pos_num_validate(value, 'y', typ="int")
        self.__y = value

    # magic methods
    def __str__(self) -> str:
        """Creates a string representation of rectangle instance

        Returns: string format of Rectangle class suitable for printing
            format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    # public methods
    def area(self) -> int:
        """Calculates the area of rectangle

        Returns: area of rectangle
        """
        return self.width * self.height

    def display(self) -> str:
        """Renders rectangle as a string

        Uses the characer '#' to render the rectangle
            - does not handle x and y
        """
        res = ""
        # render '\n' for y
        i = int(self.y)
        while i:
            res += '\n'
            i -= 1
        i = self.height
        while i:
            # render ' ' for x
            j = self.x
            while j:
                res += ' '
                j -= 1

            # render '#' for width, & repeat for height
            j = self.width
            while j:
                res += '#'
                j -= 1
            i -= 1
            if i:
                res += '\n'
        print(res, flush=True)

    def to_dictionary(self) -> dict:
        """Makes a dict representation of Rectangle
        """
        keys = ["id", "width", "height", 'x', 'y']
        rep = {}
        for key in keys:
            rep[key] = getattr(self, key)
        return rep

    def update(self, *args, **kwargs) -> None:
        """Updates class attributes

        There's no need to validate types and values as the setters
            would do that.
            kwargs are skipped if args exist and are not empty

        Args:
            args(:obj:tuple): positional arguments
            kwargs(:obj:dict): keyword arguments

        Returns: None
        """
        keys = ["id", "width", "height", 'x', 'y']

        if args and len(args):
            length = len(args)
            max = length if length < 5 else 5
            for i in range(max):
                setattr(self, keys[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)
