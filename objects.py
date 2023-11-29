#!/usr/bin/python3

class Fraction:
	def __init__(self:object, num:int, denum:int) -> None:
		if any(not isinstance(n, int) for n in (num, denum)):
			raise TypeError("numerator and denumerators must be integers")
		self.num = num
		self.denum = denum

	@staticmethod
	def gcd(a:int, b:int) -> int:
		if not b:
			return a
		return Fraction.gcd(b, a % b)

	@classmethod
	def lowest(cls:object, num:int, denum:int) -> tuple:
		gcd = cls.gcd(num, denum)
		return (num // gcd, denum // gcd)

	@property
	def reduce(self:object) -> tuple:
		gcd = type(self).gcd(self.num, self.denum)
		return (self.num // gcd, self.denum // gcd)

	def __repr__(self:object) -> str:
		return "{}/{}".format(self.num, self.denum)

#frac1 = Fraction(18, 30)
#print(frac1.gcd(frac1.num, frac1.denum))
##print(frac1.lowest(frac1.num, frac1.denum))
#print(frac1)
#print("{}/{}".format(*frac1.reduce))


class Pet:
	info = "pet animals"

	@classmethod
	def about(obj):
		Pet.info = "updated pet info"
		return "class of {}".format(obj.info)

class Dog(Pet):
	info = "dog"
	dinfo = "something about dogs"

#d = Dog()
#print(Dog.info)
#print(Dog.dinfo)


#import sys
#try:
#	print(Pet.dinfo)
#except Exception:
#	exc_type, exc_msg, exc_obj = sys.exc_info()
#	print("Exception type: {}\nException msg:{}\n".format(exc_type, exc_msg) +
#	   "object: {}".format(exc_obj))


class Num:
	def __init__(self, val):
		self.x = val

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, newval):
		if newval < 0:
			self.__x = 0
		elif newval > 1000:
			self.__x = 1000
		else:
			self.__x = newval

num = Num(-23)

print(num.x)