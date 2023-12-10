#!/usr/bin/python3
"""Unittest module for models.rectangle module
"""


# Standard imports
from importlib.machinery import SourceFileLoader as Loader
from unittest import TestCase, main

# Local imports
base_obj = Loader("base", "../../models/base.py").load_module()
rectangle = Loader("rectangle", "../../models/rectangle.py").load_module()
validators = Loader("validators", "../../validators.py").load_module()
Base = base_obj.Base
Rectangle = rectangle.Rectangle

r = Base(2)
print(r.id)


if __name__ == "___main__":
    main()