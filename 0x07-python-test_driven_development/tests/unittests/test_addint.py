#!/usr/bin/python3

import unittest
add_int = __import__("0-add_integer").add_integer

class TestAdd(unittest.TestCase):
	def test_add_int(self):
		res = add_int(3, 4)
		self.assertEqual(res, 7)
		print("add_int(int, int) completed")

	def test_none_none(self):
		with self.assertRaises(TypeError) as err:
			res = add_int(None, None)
		self.assertEqual(str(err.exception), \
				"a must be an integer or b must be an integer")
		print("add_int(None, None) completed")

	def test_str_int(self):
		with self.assertRaises(TypeError) as err:
			res = add_int("1")
		self.assertEqual(str(err.exception), \
			"a must be an integer or b must be an integer")
		print("add_int(str, int) test completed")

	def test_tuple_dict(self):
		with self.assertRaises(TypeError) as err:
			res = add_int((1, 2), {"a": 9, "b": 10})
		self.assertEqual(str(err.exception), \
			"a must be an integer or b must be an integer")
		print("add_int(tuple, dict) test completed")

	def test_result_type(self):
		res = add_int(3.8, 9.3)
		self.assertIsInstance(res, int)
		print("test type(add_int(3.8, 9.3)) complete")


if __name__ == "__main__":
	unittest.main()