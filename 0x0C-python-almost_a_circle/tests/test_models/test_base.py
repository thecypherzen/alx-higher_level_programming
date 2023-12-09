#!/usr/bin/python3
"""Unittest for base.py module
"""


from importlib.machinery import SourceFileLoader
from unittest import TestCase, main

base_module = SourceFileLoader("base", "../../models/base.py").load_module()
Base = base_module.Base


class TestBase(TestCase):
    @classmethod
    def setUpClass(cls):
        """set up class instance objects"""
        cls.base1 = Base(1)
        cls.base2 = Base()
        cls.baseneg = Base(-5)
        cls.basezero = Base(0)

    def test_id(self):
        """check instance ids"""
        with self.subTest(msg=1):
            self.assertEqual(self.base1.id, 1)
        with self.subTest(msg=2):
            self.assertEqual(self.base2.id, 1)
        with self.subTest(msg=3):
            self.assertEqual(self.baseneg.id, -5)
        with self.subTest(msg=4):
            self.assertEqual(self.basezero.id, 0)

    def test_type(self):
        """test ``types`` of objects"""
        lst = [self.base1, self.base2]
        for base in lst:
            with self.subTest(msg=lst.index(base), base=base):
                self.assertEqual(type(base).__name__, "Base")

    def test_private(self):
        """tests access to private class attribute ``__nb_objects``"""
        with self.assertRaises(AttributeError) as err:
            print(self.base1.__nb_objects)
        self.assertEqual(str(err.exception),
                         "'Base' object has no attribute" +
                         " '_TestBase__nb_objects'")


if __name__ == "__main__":
    main()
