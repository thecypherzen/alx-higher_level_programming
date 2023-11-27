#!/usr/bin/python3
"""A unittest for say_my_name function"""

say_name = __import__("3-say_my_name").say_my_name
from unittest import TestCase, main
from io import StringIO
import sys

class TestSayName(TestCase):
	#setup class
	@classmethod
	def setUpClass(cls):
		cls.file = StringIO()

	@classmethod
	def tearDownClass(cls):
		cls.file.close()

	# check 1: first_name is not a string
	def test_fn_type(self):
		with self.assertRaises(TypeError) as e:
			say_name(19)
		self.assertEqual(str(e.exception),
				   "first_name must be a string or last_name must be a string")
		print("[check 1 pass]: first_name not string caught")

	# check 2: last_name not a string
	def test_ln_type(self):
		with self.assertRaises(TypeError) as e:
			say_name("Johnson", {"a": "A"})
		self.assertEqual(str(e.exception),
				   "first_name must be a string or last_name must be a string")
		print("[check 2 pass]: last_name not string caught")

	# check 3: both not strings
	def test_both_types(self):
		with self.assertRaises(TypeError) as e:
			say_name(("abc",), True)
		self.assertEqual(str(e.exception),
				   "first_name must be a string or last_name must be a string")
		print("[check 3 pass]: both params not string caught")

	# check 4: first_name and last_name are None
	def test_both_is_None(self):
		with self.assertRaises(TypeError) as e:
			say_name(None)
		self.assertEqual(str(e.exception),
				   "first_name must be a string or last_name must be a string")
		print("[check 4 pass]: None arguments caught")

	# check 5: first_name is empty
	def test_fn_empty(self):
		stream = self.file
		if stream.tell():
			stream.truncate(0)
			stream.seek(0)
		sys.stdout = stream
		say_name("")
		output = self.file.getvalue().rstrip('\n')
		sys.stdout = sys.__stdout__
		self.assertEqual(output, "My name is  ")
		print("[check 5 pass]: first_name empty")

	# check 6: both is empty
	def test_both_empty(self):
		stream = self.file
		if stream.tell() > 0:
			stream.truncate(0)
			stream.seek(0)
		sys.stdout = stream
		say_name("", "")
		output = self.file.getvalue().rstrip('\n')
		sys.stdout = sys.__stdout__
		self.assertEqual(output, "My name is  ")
		print("[check 6 pass]: both names empty")

	# check 7: only first_name given
	def test_only_fn(self):
		stream = self.file
		if stream.tell() > 0:
			stream.truncate(0)
			stream.seek(0)
		sys.stdout = stream
		say_name("Malami")
		sys.stdout = sys.__stdout__
		output = stream.getvalue().rstrip('\n')
		self.assertEqual(output, "My name is Malami ")
		print("[check 7 pass]: only first_name given")

	# check 8: function returns None
	def test_return_none(self):
		self.assertEqual(str(say_name("A", "B")), "None")
		print("[check 8 pass]: function returns None")

	# check 9: correct greeting message on correct input
	def test_correct_output(self):
		stream = self.file
		if stream.tell():
			stream.truncate(0)
			stream.seek(0)
		sys.stdout = stream
		say_name("Kershima", "Akombo")
		sys.stdout = sys.__stdout__
		output = stream.getvalue().rstrip('\n')
		self.assertEqual(output, "My name is Kershima Akombo")
		print("[check 9 pass]: correct output gotten")

if __name__ == "__main__":
	main()
