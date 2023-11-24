#!/usr/bin/python3
import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
	import sys
	file = open("./test_file.txt", "a+")
	platform = sys.platform

	def setUp(self):
		self.customer1 = Customer("Arnold", "Ajekwe", 30000)
		self.customer2 = Customer("Hemba", "Agev", 98990.70)
		with self.assertRaises(TypeError) as err:
			self.customer3 = Customer(["dembele", 3], [9.0, 3], "fire")
		self.assertEqual(str(err.exception), "names must be of type string")
		with self.assertRaises(TypeError) as err:
			self.customer4 = Customer("Gaius", "James", 3j)
		self.assertEqual(str(err.exception), "purchase amount must be of type int or float")
		self.file.write("\nTestCase set up successfully\n")

	@classmethod
	def setUpClass(cls):
		cls.file.write("setUpClass executed\n")

	@classmethod
	def tearDownClass(cls):
		cls.file.write("tearDownClass executed\n")
		cls.file.close()

	#@unittest.skip("skipping customer_email test\n")
	def test_customer_mail(self):
		self.assertEqual(self.customer1.email, "Arnold.Ajekwe@email.com")
		self.assertEqual(self.customer2.email, "Hemba.Agev@email.com")
		self.file.write("customer_mail tested\n")

	@unittest.skipUnless(platform == "linux", "linux required")
	def test_full_name(self):
		self.assertEqual(self.customer1.full_name, "Arnold Ajekwe")
		self.assertEqual(self.customer2.full_name, "Hemba Agev")
		self.file.write("full_name tested\n")

	def test_apply_discount(self):
		self.customer1.apply_discount()
		self.customer2.apply_discount()

		self.assertEqual(self.customer1.purchase, 28500)
		self.assertEqual(self.customer2.purchase, 94041)
		#print(self.customer3.apply_discount)
		self.file.write("apply_discount tested\n")


if __name__ == "__main__":
	unittest.main()
