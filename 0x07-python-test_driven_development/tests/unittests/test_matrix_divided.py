#!/usr/bin/python3

import unittest
div_matrix = __import__("2-matrix_divided").matrix_divided

class TestMatrix(unittest.TestCase):
	# check 1: matrix is None
	def test_matrix_is_none(self):
		with self.assertRaises(TypeError) as err:
			div_matrix(None, 0)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check1 pass] matrix is None caught")

	# check 2: matrix is not a list
	def test_matrix_is_list(self):
		with self.assertRaises(TypeError) as err:
			div_matrix({"key1": 1, "key2": 2}, 3)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check2 pass] matrix not a list caught")

	# check 3: matrix is empty
	def test_matrix_is_empty(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([], 3)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check3 pass] matrix is empty caught")

	# check 4: matrix is list of list
	def test_is_list_of_lists(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([[2, 3], ("a", 3), "things", {1: 1, 2: 2}], 3)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check4 pass] matrix not a list of lists caught")

	# check 5: maxtirx has Nones
	def test_matrix_has_nones(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([[9, 9], [25.44, 19], None], 5)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check5 pass] matrix has None types caught")

	# check 6: matrix has list with Nones
	def test_marix_lists_has_nones(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([[-19], [None]], 4.55)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check6 pass] matrix has list with Nones caught")

	# check 7: matrix member empty
	def test_marix_member_empty(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([[], [55], []], 4.55)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check7 pass] matrix member empty caught")

	#check 8: matrix is list of list of numbers only
	def test_lol_of_int_or_float(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([[1, 2.0], ["str1", (1, 2)], [5, [3, 4]]], 10)
		self.assertEqual(str(err.exception),
				   "matrix must be a matrix (list of lists) of integers/floats")
		print("[check8 pass] matrix not list of " +
		"lists of numbers only caught")

	# check 9: matrix row sizes equal
	def test_matrix_row_size(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([[10, 0, -4], [9], [-1, 4, 0, 5]], 9)
		self.assertEqual(str(err.exception),
				   "Each row of the matrix must have the same size")
		print("[check9 pass] matrix rows not of same size caught")


	# check 10: div must be a number
	def test_div_is_num(self):
		with self.assertRaises(TypeError) as err:
			div_matrix([[1, 2], [3, 4], [5, 10]], "2")
		self.assertEqual(str(err.exception),
				   "div must be a number")
		print("[check10 pass] div not a number caught")

	# check 11: div is zero
	def test_div_is_zero(self):
		with self.assertRaises(ZeroDivisionError) as zee:
			div_matrix([[-1, 2, 9], [8, 99, -20]], 0)
		self.assertEqual(str(zee.exception),
				   "division by zero")
		print("[check11 pass] div is zero caught")

	# check 12: div is 1
	def test_div_is_1(self):
		res = div_matrix([[1, -5], [3, 0]], 1)
		self.assertEqual(res, [[1.00, -5.00], [3.00, 0.00]])
		print("[check12 pass] when div is 1")

	#check 13: div is float and > 0
	def test_div_pos_float(self):
		res = div_matrix([[2343, -1, -83], [-0.23, -49, -3]], 3.40)
		self.assertEqual(res, [[689.12, -0.29, -24.41],
						 [-0.07, -14.41, -0.88]])
		print("[check13 pass] when div is float and > 0")

	# check 14: div is int and  < 0
	def test_div_neg_int(self):
		res = div_matrix([[5.2, 2], [-8, -20]], -3)
		self.assertEqual(res, [[-1.73, -0.67], [2.67, 6.67]])
		print("[check14 pass] when div is int and < 0")

	# check 15: div is float and < 0
	def test_div_neg_float(self):
		res = div_matrix([[100]], -4.25)
		self.assertEqual(res, [[-23.53]])
		print("[check15 pass] when div is float and < 0")

	# check 16: precision of matrix nums after div == 2
	def test_matrix_precision(self):
		res = div_matrix([[4, 5], [-2, 1]], 2)
		for row in res:
			for i in row:
				p = len(str(i).split(".")[1])
				self.assertLessEqual(p, 2)
		print("[check16 pass] matrix row elements' precision")

	# check 17: obj returned value is a list
	def test_return_list_type(self):
		res = div_matrix([[9]], 8)
		self.assertIsInstance(res, list)
		print("[check17 pass] returned obj is a list type")

	# check 18: returned obj is different from input_matrix
	def test_return_diff_obj(self):
		matrix = [[-1], [2]]
		res = div_matrix(matrix, 3.25)
		self.assertIsNot(res, matrix)
		print("[check18 pass] returned obj is different")

	# check 19: div is None
	def test_return_diff_obj(self):
		matrix = [[-1], [2]]
		with self.assertRaises(TypeError) as err:
			div_matrix(matrix, None)
		self.assertEqual(str(err.exception), "div must be a number")
		print("[check18 pass] div is None caught")

if __name__ == "__main__":
	unittest.main()