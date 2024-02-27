#!/usr/bin/python3
"""A unittest for 1-rectangle.py"""

from unittest import TestCase, main
Rectangle = __import__("1-rectangle").Rectangle

class TestRect(TestCase):
    def setUp(self):
        self.rect1 = Rectangle(3, 4)
        with self.assertRaises(TypeError) as err:
            self.rect2 = Rectangle("a", (3))
        self.assertEqual(str(err.exception), "height must be an integer")
        print("set up success")


if __name__ == "__main__":
    main()
