#!/usr/bin/python3
""" Check """
import inspect

#rectangle_import = __import__('models.rectangle').rectangle
from models.rectangle import Rectangle

#if rectangle_import is None:
#    print("Can't import models.rectangle")
#    exit(1)

#rectangle_class = rectangle_import.__dict__.get('Rectangle')
if Rectangle is None:
    print("Can't find class Rectangle in models.rectangle")
    exit(1)
print(Rectangle)
if not inspect.isclass(Rectangle):
    print("Rectangle is not a class")
    exit(1)

from models.base import Base
print(Base)
if not issubclass(Rectangle, Base):
    print("Rectangle is not a subclass of Base")
    exit(1)

print("OK", end="")

