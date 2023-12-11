#!/usr/bin/python3
#!/usr/bin/python3
"""Unittest for square module
"""

# Standard imports:
import os
import sys
from unittest import TestCase, main

# Local imports
from square import Square

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
            res = "[Square] (2) 0/0 - 3/3"
            self.assertEqual(str(sq), res)
        # all args given
        with self.subTest(msg="init-2"):
            sq = Square(3, 4, 5, 12)
            res = "[Square] (12) 4/5 - 3/3"
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



if __name__ == "__main__":
    main()