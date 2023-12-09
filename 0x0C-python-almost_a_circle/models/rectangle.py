#!/usr/bin/python3
"""0x0C. Python - Almost a circle - Tasks 2-9

This module implements incremental solutions to tasks 2 through 9
of this project.

Class(s):
    Rectange: a class defining a rectangle
Functions(s):

"""


# Standard imports
from importlib.machinery import SourceFileLoader as Loader

# Local imports
from base import Base

validators = Loader("validators", "../validators.py").load_module()

class Rectangle(Base):
    """Defines a rectangle

    Attributes:
        width (:obj: `getter`, `setter`): getter/setter of width
        height (:obj: `getter`, `setter`): getter/setter of height
        x (:obj: `getter`, `setter`): getter/setter of property x
        y (:obj: `getter`, `setter`): getter/setter of property y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises instance of rectangle

        Args:
            width (`any`): rectangle's width
            height (`any`): rectangle's height
            x (`any`): position on x axis
            y (`any`): position on y axis
            id(`any`): instance's id number
        """
        validators.gt_zero_validate(width, "width", typ="int")
        validators.gt_zero_validate(height, "height", typ="int")
        validators.pos_num_validate(x, 'x')
        validators.pos_num_validate(y, 'y')
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # private attribute setters
    @property
    def width(self):
        """:obj `any`: Getter of width property

        Setter Args:
            value(any): update value of `width` to `value`
        """
        return self.__width

    @property
    def height(self):
        """:obj: `any`: Getter of height property

        Setter Args:
            value(any): update value of `height` to `value`
        """
        return self.__height

    @property
    def x(self):
        """:obj: `any`: Getter of x property

        Setter Args:
            value(any): update value of `x` to `value`
        """
        return self.__x

    @property
    def y(self):
        """:obj: `any`: Getter of y property

        Setter Args:
            value(any): update value of`y` to `value`
        """
        return self.__y

    # private attribute setters
    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
