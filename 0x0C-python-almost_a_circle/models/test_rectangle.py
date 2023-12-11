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
        cls.rect3 = Rectangle(4, 3, 13)
        cls.rect4 = Rectangle(1, 9, y=8, id=-2.2)
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
        with self.subTest(msg="rect4(1,9)"):
            print(self.rect4.area(), file=self.stream_w, end="", flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '9')

    # ******* display test case *******
    def test_display(self):
        # rectangle 1
        with self.subTest(msg="rect1(7,5)"):
            # display rectangle to stream & check num of lines
            sys.stdout = self.stream_w
            self.rect1.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            x = self.rect1.x
            y = self.rect1.y
            self.assertEqual(length, 5+y)
            if y:
                for i in range(y):
                    with self.subTest(msg=f"i={i}(y={y})"):
                        self.assertEqual(lines[i], '\n')
                del lines[0:y-1]

            # check length of each line and validate 'x' and '#'
            for i in range(length - y):
                with self.subTest(msg=f"line:{i}y:{y}"):
                    line = lines[i].rstrip('\n')
                    self.assertEqual(len(line), 7+x)

                    # check num of spaces == x
                    for j in range(x):
                        with self.subTest(msg=f"x-check[{j}]"):
                            self.assertEqual(line[j], ' ')

                    # check for '#' chars after x chars left in line
                    for j in range(x, len(line)):
                        with self.subTest(msg=f"#-check[{j}]"):
                            self.assertEqual(line[j], '#')
        # rectangle2
        with self.subTest(msg="rect2(2,10)"):
            # display rectangle to stream & check num of lines
            sys.stdout = self.stream_w
            self.rect2.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            x = self.rect2.x
            y = self.rect2.y
            self.assertEqual(length, 10+y)
            # check num of new_lines == y if y
            if y:
                for i in range(y):
                    with self.subTest(msg=f"i={i}(y={y})"):
                        self.assertEqual(lines[i], '\n')
                del lines[0:y]
            # check length of each line and validate 'x' and '#'
            for i in range(length - y):
                with self.subTest(msg=f"line:{i}y:{y}"):
                    line = lines[i].rstrip('\n')
                    self.assertEqual(len(line), 2+x)

                    # check num of spaces == x
                    for j in range(x):
                        with self.subTest(msg=f"x-check[{j}]"):
                            self.assertEqual(line[j], ' ')

                    # check for '#' chars after x chars left in line
                    for j in range(x, len(line)):
                        with self.subTest(msg=f"#-check[{j}]"):
                            self.assertEqual(line[j], '#')
        # rectangle 3
        with self.subTest(msg="rect3(4,3)"):
            # display rectangle to stream & check num of lines
            sys.stdout = self.stream_w
            self.rect3.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            x = self.rect3.x
            y = self.rect3.y
            self.assertEqual(length, 3+y)
            # check num of new_lines == y if y
            if y:
                for i in range(y):
                    with self.subTest(msg=f"i={i}(y={y})"):
                        self.assertEqual(lines[i], '\n')
                del lines[0:y]

            # check length of each line and validate 'x' and '#'
            for i in range(length - y):
                with self.subTest(msg=f"line:{i}y:{y}"):
                    line = lines[i].rstrip('\n')
                    self.assertEqual(len(line), 4+x)

                    # check num of spaces == x
                    for j in range(x):
                        with self.subTest(msg=f"x-check[{j}]"):
                            self.assertEqual(line[j], ' ')

                    # check for '#' chars after x chars left in line
                    for j in range(x, len(line)):
                        with self.subTest(msg=f"#-check[{j}]"):
                            self.assertEqual(line[j], '#')
        # rectangle 4
        with self.subTest(msg="rect4(1,9)"):
            # display rectangle to stream & check num of lines
            sys.stdout = self.stream_w
            self.rect4.display()
            sys.stdout = sys.__stdout__
            lines = self.stream_r.readlines()
            length = len(lines)
            x = self.rect4.x
            y = self.rect4.y
            self.assertEqual(length, 9+y)

            # check num of new_lines == y if y
            if y:
                for i in range(y):
                    with self.subTest(msg=f"i={i}(y={y})"):
                        self.assertEqual(lines[i], '\n')
                del lines[0:y]

            # check length of each line and validate 'x' and '#'
            for i in range(length - y):
                with self.subTest(msg=f"line:{i}y:{y}"):
                    line = lines[i].rstrip('\n')
                    self.assertEqual(len(line), 1+x)

                    # check num of spaces == x
                    for j in range(x):
                        with self.subTest(msg=f"x-check[{j}]"):
                            self.assertEqual(line[j], ' ')

                    # check for '#' chars after x chars left in line
                    for j in range(x, len(line)):
                        with self.subTest(msg=f"#-check[{j}]"):
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
        with self.subTest(msg="height == 9"):
            print(self.rect4.height, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "9")

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

    # ******* setters test cases *******
    def test_setters(self):
        newrect = Rectangle(5, 8)

        # width setter checks
        with self.subTest(msg=f"sttr1:w=float"):
            with self.assertRaises(TypeError) as err:
                newrect.width = 1.2
                msg = str(err.exception)
                self.assertEqual(msg, "width must be an integer")
        with self.subTest(msg=f"sttr2:w=0"):
            with self.assertRaises(ValueError) as err:
                newrect.width = 0
                msg = str(err.exception)
                self.assertEqual(msg, "width must be > 0")
        with self.subTest(msg=f"sttr3:w<0"):
            with self.assertRaises(ValueError) as err:
                newrect.width = -3
                msg = str(err.exception)
                self.assertEqual(msg, "width must be > 0")
        with self.subTest(msg=f"sttr4:w=None"):
            with self.assertRaises(TypeError) as err:
                newrect.width = None
                msg = str(err.exception)
                self.assertEqual(msg, "width must be an integer")
        with self.subTest(msg=f"sttr5:w=int"):
            newrect.width = 8
            self.assertEqual(newrect.width, 8)

        # height setter checks
        with self.subTest(msg=f"sttr6:h=float"):
            with self.assertRaises(TypeError) as err:
                newrect.height = 0.0
                msg = str(err.exception)
                self.assertEqual(msg, "height must be an integer")
        with self.subTest(msg=f"sttr7:h=0"):
            with self.assertRaises(ValueError) as err:
                newrect.height = 0
                msg = str(err.exception)
                self.assertEqual(msg, "height must be > 0")
        with self.subTest(msg=f"sttr8:h<0"):
            with self.assertRaises(ValueError) as err:
                newrect.height = -3
                msg = str(err.exception)
                self.assertEqual(msg, "height must be > 0")
        with self.subTest(msg=f"sttr9:h=None"):
            with self.assertRaises(TypeError) as err:
                newrect.height = None
                msg = str(err.exception)
                self.assertEqual(msg, "height must be an integer")
        with self.subTest(msg=f"sttr10:h=int"):
            newrect.height = 5
            self.assertEqual(newrect.height, 5)

        # x setter checks
        with self.subTest(msg=f"sttr11:x=float"):
            with self.assertRaises(TypeError) as err:
                newrect.x = 1.2
                msg = str(err.exception)
                self.assertEqual(msg, "x must be an integer")
        with self.subTest(msg=f"sttr12:x<0"):
            with self.assertRaises(ValueError) as err:
                newrect.x = -3
                msg = str(err.exception)
                self.assertEqual(msg, "x must be >= 0")
        with self.subTest(msg=f"sttr13:x=None"):
            with self.assertRaises(TypeError) as err:
                newrect.x = None
                msg = str(err.exception)
                self.assertEqual(msg, "x must be an integer")
        with self.subTest(msg=f"sttr14:x=int"):
            newrect.x = 6
            self.assertEqual(newrect.x, 6)

        # y setter checks
        with self.subTest(msg=f"sttr15:y=float"):
            with self.assertRaises(TypeError) as err:
                newrect.y = 22.2
                msg = str(err.exception)
                self.assertEqual(msg, "y must be an integer")
        with self.subTest(msg=f"sttr16:y<0"):
            with self.assertRaises(ValueError) as err:
                newrect.y = -3
                msg = str(err.exception)
                self.assertEqual(msg, "y must be >= 0")
        with self.subTest(msg=f"sttr17:y=None"):
            with self.assertRaises(TypeError) as err:
                newrect.y = None
                msg = str(err.exception)
                self.assertEqual(msg, "y must be an integer")
        with self.subTest(msg=f"sttr18:y=int"):
            newrect.y = 3
            self.assertEqual(newrect.y, 3)
        with self.subTest(msg=f"sttr19:id"):
            newrect.id = -3
            self.assertEqual(newrect.id, -3)

    # ******* __str__ test cases *******
    # [Rectangle] (<id>) <x>/<y> - <width>/<height>
    def test_str_res(self):
        with self.subTest(msg="rect1(7,5)"):
            res = str(self.rect1)
            self.assertEqual(res, "[Rectangle] (1) 0/0 - 7/5")
        with self.subTest(msg="rect2(2,10,4,3,11)"):
            res = str(self.rect2)
            self.assertEqual(res, "[Rectangle] (11) 4/3 - 2/10")
        with self.subTest(msg="rect3(4,3,13)"):
            res = str(self.rect3)
            self.assertEqual(res, "[Rectangle] (2) 13/0 - 4/3")
        with self.subTest(msg="rect4(1,9,y=8,id=-2.2)"):
            res = str(self.rect4)
            self.assertEqual(res, "[Rectangle] (-2.2) 0/8 - 1/9")

    # ******* update test cases *******
    def test_update(self):
        new_rect = Rectangle(1, 4)

        with self.subTest(msg="upd-1"):
            new_rect.update(20, 12)
            res = str(new_rect)
            self.assertEqual(res, "[Rectangle] (20) 0/0 - 12/4")

        with self.subTest(msg="upd-2"):
            new_rect.update(5)
            res = str(new_rect)
            self.assertEqual(res, "[Rectangle] (5) 0/0 - 12/4")

        with self.subTest(msg="upd-3"):
            new_rect.update(x=3, y=16)
            res = str(new_rect)
            self.assertEqual(res, "[Rectangle] (5) 3/16 - 12/4")

        with self.subTest(msg="upd-4"):
            new_rect.update(width=5, height=9)
            res = str(new_rect)
            self.assertEqual(res, "[Rectangle] (5) 3/16 - 5/9")

        with self.subTest(msg="upd-5"):
            new_rect.update(2, 3, 4, 5, 6)
            res = str(new_rect)
            self.assertEqual(res, "[Rectangle] (2) 5/6 - 3/4")


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
        with self.subTest(msg="width == 1"):
            print(self.rect4.width, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "1")

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
        with self.subTest(msg="x == 13"):
            print(self.rect3.x, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, "13")
        with self.subTest(msg="x == 0"):
            print(self.rect4.x, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '0')

    # test x is Dict
    def test_x_is_dict(self):
        with self.subTest(msg="x is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, {1:2})
            self.assertEqual(str(err.exception), "x must be an integer")

    # test x is Float
    def test_x_is_float(self):
        with self.subTest(msg="x is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, 2.9)
            self.assertEqual(str(err.exception), "x must be an integer")

    # test x is hidden
    def test_x_is_hidden(self):
        with self.subTest(msg="hidden x"):
            with self.assertRaises(AttributeError) as err:
                print(self.rect1.__x)
            self.assertEqual(str(err.exception),
                            "'Rectangle' object has no attribute" +
                            " '_TestRect__x'")

    # test x is None
    def test_x_is_none(self):
        with self.subTest(msg="x is None"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, None, 3)
            self.assertEqual(str(err.exception), "x must be an integer")

    # test x is string
    def test_x_is_string(self):
        with self.subTest(msg="x is string"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, "2")
            self.assertEqual(str(err.exception), "x must be an integer")

    # test x is tuple
    def test_x_is_tuple(self):
        with self.subTest(msg="x tuple"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(1, 2, (2, 4), 4)
            self.assertEqual(str(err.exception), "x must be an integer")

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
        with self.subTest(msg="y == 8"):
            print(self.rect4.y, end="", file=self.stream_w, flush=True)
            res = self.stream_r.read()
            self.assertEqual(res, '8')

    # test y is Dict
    def test_y_is_dict(self):
        with self.subTest(msg="y is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, 9, {1:2})
            self.assertEqual(str(err.exception), "y must be an integer")

    # test y is Float
    def test_x_is_float(self):
        with self.subTest(msg="x is dict"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, y=2.9)
            self.assertEqual(str(err.exception), "y must be an integer")

    # test y is hidden
    def test_y_is_hidden(self):
        with self.subTest(msg="hidden y"):
            with self.assertRaises(AttributeError) as err:
                print(self.rect1.__y)
            self.assertEqual(str(err.exception),
                            "'Rectangle' object has no attribute" +
                            " '_TestRect__y'")

    # test y is None
    def test_y_is_none(self):
        with self.subTest(msg="y is None"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, 3, None)
            self.assertEqual(str(err.exception), "y must be an integer")

    # test y is string
    def test_y_is_string(self):
        with self.subTest(msg="y is string"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(2, 3, 9, '2')
            self.assertEqual(str(err.exception), "y must be an integer")

    # test y is tuple
    def test_y_is_tuple(self):
        with self.subTest(msg="y tuple"):
            with self.assertRaises(TypeError) as err:
                _ = Rectangle(1, 2, 4, (2, 4))
            self.assertEqual(str(err.exception), "y must be an integer")

    # test y is < 0
    def test_y_ltzero(self):
        with self.subTest(msg="y < 0"):
            with self.assertRaises(ValueError) as err:
                _ = Rectangle(1, 2, 2, -4)
            self.assertEqual(str(err.exception), "y must be >= 0")


if __name__ == "___main__":
    main()