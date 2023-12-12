#!/usr/bin/python3

"""Unittest for square module
"""

# Standard imports:
from importlib.machinery import SourceFileLoader as Loader
import os
import sys
from unittest import TestCase, main

# Local imports
path = os.path.realpath("../../models/square.py")
square = Loader("square", path).load_module()
Square = square.Square


class TestSquare(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sq = Square(9)
        cls.stream_w = open("streamio", "w")
        cls.stream_r = open("streamio", "r")
        cls.stream_a = open("streamio", "a+")

    @classmethod
    def tearDownClass(cls):
        cls.stream_w.close()
        cls.stream_r.close()
        cls.stream_a.close()
        if os.path.exists("streamio"):
            os.remove("streamio")

    def test_area(self):
        self.assertEqual(self.sq.area(), 81)

    def test_display(self):
        with self.subTest(msg="dsp-1"):
            sq1 = Square(3, 4, 5)
            x = sq1.x
            y = sq1.y
            sys.stdout = self.stream_w
            sq1.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            self.assertEqual(length, sq1.height+y)
            if y:
                for i in range(y):
                    with self.subTest(msg=f"ychk-{i}"):
                        self.assertEqual(lines[i], '\n')
                del lines[0:y]
            for i in range(length - y):
                line = lines[i]
                for j in range(x):
                    with self.subTest(msg=f"xchk-{j}"):
                        self.assertEqual(line[j], ' ')
                for j in range(x, length-y):
                    with self.subTest(msg=f"#chk-{j}"):
                        self.assertEqual(line[j], '#')

    def test_init(self):
        # size and id given
        with self.subTest(msg="init-1"):
            sq = Square(3, id=2)
            res = "[Square] (2) 0/0 - 3"
            self.assertEqual(str(sq), res)
        # all args given
        with self.subTest(msg="init-2"):
            sq = Square(3, 4, 5, 12)
            res = "[Square] (12) 4/5 - 3"
            self.assertEqual(str(sq), res)
        # size == float
        with self.subTest(msg="init-3"):
            with self.assertRaises(TypeError) as err:
                sq = Square(3.0, 4, 5, 12)
                res = "width must be an integer"
                self.assertEqual(str(err.exception), res)
        # size == 0
        with self.subTest(msg="init-4"):
            with self.assertRaises(ValueError) as err:
                sq = Square(0, 4, 5, 12)
                res = "width must be > 0"
                self.assertEqual(str(err.exception), res)
        # x < 0
        with self.subTest(msg="init-5"):
            with self.assertRaises(ValueError) as err:
                sq = Square(6, -4, 5, 12)
                res = "x must be >= 0"
                self.assertEqual(str(err.exception), res)
        # y < 0
        with self.subTest(msg="init-6"):
            with self.assertRaises(ValueError) as err:
                sq = Square(6, 4, -5, 12)
                res = "y must be >= 0"
                self.assertEqual(str(err.exception), res)
        # size == None
        with self.subTest(msg="init-7"):
            with self.assertRaises(TypeError) as err:
                sq = Square(None, 4, 5, 12)
                res = "width must be an integer"
                self.assertEqual(str(err.exception), res)

    def test_size(self):
        # get size as expected
        with self.subTest(msg="sz-1"):
            self.assertEqual(self.sq.size, 9)
        # set size new value
        with self.subTest(msg="sz-2"):
            self.sq.size = 5
            # check size change
            with self.subTest(msg="sz-2(1)"):
                self.assertEqual(self.sq.size, 5)

            # check other sq str
            with self.subTest(msg="sz-2(2)"):
                res = "[Square] (1) 0/0 - 5"
                self.assertEqual(str(self.sq), res)

            # check other sq width
            with self.subTest(msg="sz-2(3)"):
                res = "[Square] (1) 0/0 - 5"
                self.assertEqual(self.sq.width, 5)

            # check other sq height
            with self.subTest(msg="sz-2(4)"):
                self.assertEqual(self.sq.height, 5)

    def test_to_dictionary(self):
        with self.subTest(msg="dic-1"):
            d1 = self.sq.to_dictionary()
            # check type(d1) is dict
            with self.subTest(msg="d1-a:type-chk"):
                self.assertEqual(d1.__class__.__name__, "dict")

            # check d1 has excatly 4 values
            with self.subTest(msg="d1-b:size-chk"):
                self.assertEqual(len(d1), 4)

            keys = ["id", "size", 'x', 'y']
            vals = [1, 5, 0, 0]

            # check keys in d1 match expected attribute names
            for key in keys:
                with self.subTest(msg="d1-c:key2key-chk"):
                    self.assertEqual(key in d1, True)

            # check values of each key in d1 is as expected
            for key in keys:
                with self.subTest(msg="d1-d:key2val-chk"):
                    self.assertEqual(d1[key], vals[keys.index(key)])

        with self.subTest(msg="dic-2"):
            self.sq.update(id=19, x=1, y=3, size=7)
            d1 = self.sq.to_dictionary()

            # check type(d1) is dict
            with self.subTest(msg="d2-a:type-chk"):
                self.assertEqual(d1.__class__.__name__, "dict")

            # check d1 has excatly 4 values
            with self.subTest(msg="d2-b:size-chk"):
                self.assertEqual(len(d1), 4)

            keys = ["id", "size", 'x', 'y']
            vals = [19, 7, 1, 3]

            # check keys in d1 match expected attribute names
            for key in keys:
                with self.subTest(msg="d2-c:key2key-chk"):
                    self.assertEqual(key in d1, True)

            # check values of each key in d1 is as expected
            for key in keys:
                with self.subTest(msg="d2-d:key2val-chk"):
                    self.assertEqual(d1[key], vals[keys.index(key)])

    def test_update(self):
        # only args id
        with self.subTest(msg="upd-1"):
            self.sq.update(9)
            res = "[Square] (9) 1/3 - 7"
            self.assertEqual(str(self.sq), res)
        # only args id, size
        with self.subTest(msg="upd-2"):
            self.sq.update(12, 13)
            res = "[Square] (12) 1/3 - 13"
            self.assertEqual(str(self.sq), res)
        # only kwargs x
        with self.subTest(msg="upd-3"):
            self.sq.update(x=4)
            res = "[Square] (12) 4/3 - 13"
            self.assertEqual(str(self.sq), res)
        # kwargs id, y
        with self.subTest(msg="upd-4"):
            self.sq.update(y=9, id=24)
            res = "[Square] (24) 4/9 - 13"
            self.assertEqual(str(self.sq), res)


if __name__ == "__main__":
    main()
