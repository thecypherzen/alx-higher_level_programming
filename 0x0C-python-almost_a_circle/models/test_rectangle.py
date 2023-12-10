#!/usr/bin/python3
"""Unittest module for models.rectangle module
"""


# Standard imports
from unittest import TestCase, main
import os
import sys

# Local imports
from base import Base
from rectangle import Rectangle


class TestRect(TestCase):
    # test rectangle inherits from Base
    @classmethod
    def setUpClass(cls) -> None:
        """Set up default test objects"""
        cls.rect1 = Rectangle(7, 5)
        cls.rect2 = Rectangle(2, 10, 4, 3, 11)
        cls.rect3 = Rectangle(4, 3, 2.2, 0)
        cls.rect4 = Rectangle(699, 1030, 3.3, 2.9, -2.2)
        cls.stream_w = open("stream.io", 'w', encoding="utf-8")
        cls.stream_r = open("stream.io", 'r', encoding="utf-8")
        cls.stream_a = open("stream.io", "a+", encoding="utf-8")

    @classmethod
    def tearDownClass(cls) -> None:
        """Teardown classes"""
        cls.stream_a.close()
        cls.stream_r.close()
        cls.stream_w.close()
        if os.path.exists("stream.io"):
            os.remove("stream.io")

    # ******* area test cases *******
    def test_area_as_expected(self):
        with self.subTest(msg="rect1(7,5)"):
            print(self.rect1.area(), file=self.stream_w, end="", flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "35")
        with self.subTest(msg="rect2(2,10)"):
            print(self.rect2.area(), file=self.stream_w, end="", flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "20")
        with self.subTest(msg="rect3(4,3)"):
            print(self.rect3.area(), file=self.stream_w, end="", flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "12")
        with self.subTest(msg="rect4(699,1030)"):
            print(self.rect4.area(), file=self.stream_w, end="", flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "719970")

    # ******* display test case *******
    def test_display(self):
        with self.subTest(msg="rect1(7,5)"):
            sys.stdout = self.stream_w
            self.rect1.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            self.assertEqual(length, 5)
            for i in range(length):
                line = lines[i].rstrip('\n')
                with self.subTest(msg=f"i={i}"):
                    self.assertEqual(len(line), 7)
                    for j in range(len(line)):
                        with self.subTest(msg=f"line[{j}]"):
                            self.assertEqual(line[j], '#')

        with self.subTest(msg="rect2(2,10)"):
            sys.stdout = self.stream_w
            self.rect2.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            self.assertEqual(length, 10)
            for i in range(length):
                line = lines[i].rstrip('\n')
                with self.subTest(msg=f"i={i}"):
                    self.assertEqual(len(line), 2)
                    for j in range(len(line)):
                        with self.subTest(msg=f"line[{j}]"):
                            self.assertEqual(line[j], '#')

        with self.subTest(msg="rect3(4,3)"):
            sys.stdout = self.stream_w
            self.rect3.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            self.assertEqual(length, 3)
            for i in range(length):
                line = lines[i].rstrip('\n')
                with self.subTest(msg=f"i={i}"):
                    self.assertEqual(len(line), 4)
                    for j in range(len(line)):
                        with self.subTest(msg=f"line[{j}]"):
                            self.assertEqual(line[j], '#')

        with self.subTest(msg="rect4(699,1030)"):
            r = Rectangle(13, 1)
            sys.stdout = self.stream_w
            r.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            self.assertEqual(length, 1)
            for i in range(length):
                line = lines[i].rstrip('\n')
                with self.subTest(msg=f"i={i}"):
                    self.assertEqual(len(line), 13)
                    for j in range(len(line)):
                        with self.subTest(msg=f"line[{j}]"):
                            self.assertEqual(line[j], '#')

    # ******* id test cases *******
    # test id expected
    def test_id_as_expected(self):
        with self.subTest(msg="id not given"):
            print(self.rect1.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '1')
        with self.subTest(msg="id == 11"):
            print(self.rect2.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "11")
        with self.subTest(msg="id not given"):
            print(self.rect3.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '2')
        with self.subTest(msg="id == -2.2"):
            print(self.rect4.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "-2.2")

    # test id not validated
    def test_id_not_validated(self):
        with self.subTest(msg="id is string"):
            obj = Rectangle(1, 2, 3, 4, "abc")
            print(obj.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "abc")

        with self.subTest(msg="id is tuple"):
            obj = Rectangle(1, 2, 3, 4, (1, 2))
            print(obj.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "(1, 2)")

        with self.subTest(msg="id is dict"):
            obj = Rectangle(1, 2, 3, 4, {'a':1, 'b':2})
            print(obj.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "{'a': 1, 'b': 2}")

        with self.subTest(msg="id is set"):
            obj = Rectangle(1, 2, 3, 4, {2, 3})
            print(obj.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "{2, 3}")

        with self.subTest(msg="id is float"):
            obj = Rectangle(1, 2, 3, 4, 12.93)
            print(obj.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "12.93")

        with self.subTest(msg="id is bool"):
            obj = Rectangle(1, 2, 3, 4, True)
            print(obj.id, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "True")


    # ******* height test cases *******
    # test height expected
    #cls.rect4 = Rectangle(699, 1030, 3.3, 2.9, -2.2)
    def test_height_as_expected(self):
        with self.subTest(msg="height == 5"):
            print(self.rect1.height, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '5')
        with self.subTest(msg="height == 10"):
            print(self.rect2.height, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '10')
        with self.subTest(msg="height == 3"):
            print(self.rect3.height, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '3')
        with self.subTest(msg="height == 1030"):
            print(self.rect4.height, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "1030")

    # test height is hidden
    def test_height_hidden(self):
        with self.subTest(msg="height hidden"):
            with self.assertRaises(AttributeError) as err:
                print(self.rect1.__height)
            self.assertEqual(str(err.exception),
                            "'Rectangle' object has no attribute" +
                            " '_TestRect__height'")

    #test height is dict
    def test_height_is_dict(self):
        with self.subTest(msg="height is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, {2:3, 3:9}, 2, 3)
            self.assertEqual(str(err.exception), "height must be an integer")

    # test height is float
    def test_height_is_float(self):
        with self.subTest(msg="height is float"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 1.9, 2, 3)
            self.assertEqual(str(err.exception), "height must be an integer")

    # test height is None
    def test_height_is_none(self):
        with self.subTest(msg="height is None"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, None, 9, 3)
            self.assertEqual(str(err.exception), "height must be an integer")

    # test height is set
    def test_height_is_set(self):
        with self.subTest(msg="x is set"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, {10, 11}, 2, 4)
            self.assertEqual(str(err.exception), "height must be an integer")

    # test height is string
    def test_height_is_string(self):
        with self.subTest(msg="x is string"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, '2', 2, 4)
            self.assertEqual(str(err.exception), "height must be an integer")

    # test height is tuple
    def test_height_is_tuple(self):
        with self.subTest(msg="height tuple"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(1, (1,), (2, 4), 4)
            self.assertEqual(str(err.exception), "height must be an integer")

    # test height < zero
    def test_height_lt_zero(self):
        with self.subTest(msg="height < 0"):
            with self.assertRaises(ValueError) as err:
                _ = Rectangle(1, -4, (2, 4), 4)
            self.assertEqual(str(err.exception), "height must be > 0")

    # height is missing
    def test_height_missing(self):
        with self.subTest(self):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(1)
            s = str(err.exception)
            m = "__init__() missing 1 required positional argument: 'height'"
            self.assertEqual(s, m)

    # test height is zero
    def test_height_is_zero(self):
        with self.subTest(msg="height zero"):
            with self.assertRaises(ValueError) as err:
                _ = Rectangle(1, 0, (2, 4), 4)
            self.assertEqual(str(err.exception), "height must be > 0")

    # ******* __str__ test cases *******
    # [Rectangle] (<id>) <x>/<y> - <width>/<height>
    def test_str_res(self):
        with self.subTest(msg="rect1(7,5)"):
            res = str(self.rect1)
            self.assertEqual(res, "[Rectangle] (1) 0/0 - 7/5")
        with self.subTest(msg="rect2(2,10,4,3,11)"):
            res = str(self.rect2)
            self.assertEqual(res, "[Rectangle] (11) 4/3 - 2/10")
        with self.subTest(msg="rect3(4,3,2.2,0)"):
            res = str(self.rect3)
            self.assertEqual(res, "[Rectangle] (2) 2.2/0 - 4/3")
        with self.subTest(msg="rect4(699,1030,3.3,2.9,-2.2)"):
            res = str(self.rect4)
            self.assertEqual(res, "[Rectangle] (-2.2) 3.3/2.9 - 699/1030")
        with self.subTest(msg="rect4(9,10,30,id=19)"):
            rect = Rectangle(9, 10, 30, id=19)
            res = str(rect)
            self.assertEqual(res, "[Rectangle] (19) 30/0 - 9/10")

    # ******* width test cases *******
    # test width as expected
    def test_width_as_expected(self):
        with self.subTest(msg="width == 7"):
            print(self.rect1.width, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '7')
        with self.subTest(msg="width == 2"):
            print(self.rect2.width, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '2')
        with self.subTest(msg="width == 4"):
            print(self.rect3.width, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '4')
        with self.subTest(msg="width == 699"):
            print(self.rect4.width, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "699")

    # test width is hidden
    def test_width_hidden(self):
        with self.subTest(msg="width hidden"):
            with self.assertRaises(AttributeError) as err:
                print(self.rect1.__width)
            self.assertEqual(str(err.exception),
                            "'Rectangle' object has no attribute" +
                            " '_TestRect__width'")

    #test width is dict
    def test_width_is_dict(self):
        with self.subTest(msg="width is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle({2:3, 3:9}, 2, 2, 3)
            self.assertEqual(str(err.exception), "width must be an integer")

    # test width is float
    def test_width_is_float(self):
        with self.subTest(msg="width is float"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2.3, 1, 2, 3)
            self.assertEqual(str(err.exception), "width must be an integer")

    # test width is None
    def test_width_is_none(self):
        with self.subTest(msg="width is None"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(None, 2, 9, 3)
            self.assertEqual(str(err.exception), "width must be an integer")

    # test width is set
    def test_width_is_set(self):
        with self.subTest(msg="x is set"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle({10, 11}, 2, 2, 4)
            self.assertEqual(str(err.exception), "width must be an integer")

    # test width is string
    def test_width_is_string(self):
        with self.subTest(msg="x is string"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle('2', 3, 2, 4)
            self.assertEqual(str(err.exception), "width must be an integer")

    # test width is tuple
    def test_width_is_tuple(self):
        with self.subTest(msg="width tuple"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle((1,), 1, (2, 4), 4)
            self.assertEqual(str(err.exception), "width must be an integer")

    # test width < zero
    def test_width_lt_zero(self):
        with self.subTest(msg="width < 0"):
            with self.assertRaises(ValueError) as err:
                _ = Rectangle(-1, 4, (2, 4), 4)
            self.assertEqual(str(err.exception), "width must be > 0")

    # width is missing
    def test_width_missing(self):
        with self.subTest(self):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(height=2)
            s = str(err.exception)
            m = "__init__() missing 1 required positional argument: 'width'"
            self.assertEqual(s, m)

    # test width is zero
    def test_width_is_zero(self):
        with self.subTest(msg="width == 0"):
            with self.assertRaises(ValueError) as err:
                _ = Rectangle(0, 1, (2, 4), 4)
            self.assertEqual(str(err.exception), "width must be > 0")



    # ******* x test cases *******
    # test x as expected
    def test_x_as_expected(self):
        with self.subTest(msg="x == 0"):
            print(self.rect1.x, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '0')
        with self.subTest(msg="x == 4"):
            print(self.rect2.x, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '4')
        with self.subTest(msg="x == 2.2"):
            print(self.rect3.x, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '2.2')
        with self.subTest(msg="x == 3.3"):
            print(self.rect4.x, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '3.3')

    # test x is hidden
    def test_x_is_hidden(self):
        with self.subTest(msg="hidden x"):
            with self.assertRaises(AttributeError) as err:
                print(self.rect1.__x)
            self.assertEqual(str(err.exception),
                            "'Rectangle' object has no attribute" +
                            " '_TestRect__x'")

    # test x is Dict
    def test_x_is_dict(self):
        with self.subTest(msg="x is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, {1:2})
            self.assertEqual(str(err.exception), "x must be a number")

    # test x is None
    def test_x_is_none(self):
        with self.subTest(msg="x is None"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, None, 3)
            self.assertEqual(str(err.exception), "x must be a number")

    # test x is string
    def test_x_is_string(self):
        with self.subTest(msg="x is string"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, "2")
            self.assertEqual(str(err.exception), "x must be a number")

    # test x is tuple
    def test_x_is_tuple(self):
        with self.subTest(msg="x tuple"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(1, 2, (2, 4), 4)
            self.assertEqual(str(err.exception), "x must be a number")

    # test x is < 0
    def test_x_ltzero(self):
        with self.subTest(msg="x < 0"):
            with self.assertRaises(ValueError) as err:
                _ = Rectangle(1, 2, -2, 4)
            self.assertEqual(str(err.exception), "x must be >= 0")


    # ******* y test cases *******
    # test y as expected
    def test_y_as_expected(self):
        with self.subTest(msg="y == 0"):
            print(self.rect1.y, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '0')
        with self.subTest(msg="y == 3"):
            print(self.rect2.y, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '3')
        with self.subTest(msg="y == 0"):
            print(self.rect3.y, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '0')
        with self.subTest(msg="y == 2.9"):
            print(self.rect4.y, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '2.9')

    # test y is hidden
    def test_y_is_hidden(self):
        with self.subTest(msg="hidden y"):
            with self.assertRaises(AttributeError) as err:
                print(self.rect1.__y)
            self.assertEqual(str(err.exception),
                            "'Rectangle' object has no attribute" +
                            " '_TestRect__y'")

    # test y is Dict
    def test_y_is_dict(self):
        with self.subTest(msg="y is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, 9, {1:2})
            self.assertEqual(str(err.exception), "y must be a number")

    # test y is None
    def test_y_is_none(self):
        with self.subTest(msg="y is None"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, 3, None)
            self.assertEqual(str(err.exception), "y must be a number")

    # test y is string
    def test_y_is_string(self):
        with self.subTest(msg="y is string"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, 9, '2')
            self.assertEqual(str(err.exception), "y must be a number")

    # test y is tuple
    def test_y_is_tuple(self):
        with self.subTest(msg="y tuple"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(1, 2, 4, (2, 4))
            self.assertEqual(str(err.exception), "y must be a number")

    # test y is < 0
    def test_y_ltzero(self):
        with self.subTest(msg="y < 0"):
            with self.assertRaises(ValueError) as err:
                _ = Rectangle(1, 2, 2, -4)
            self.assertEqual(str(err.exception), "y must be >= 0")




if __name__ == "___main__":
    main()