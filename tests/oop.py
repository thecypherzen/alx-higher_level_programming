#!/usr/bin/python3

class Subject():
	total = 0
	__accredited = 2001

	def __init__(self, name, weight=1):
		self.creditLoad = weight
		self.name = name
		Subject.total += 1

	@classmethod
	def count(self):
		print("{}".format(self.total))

math = Subject("Math")
biology = Subject("Biology")
biology.students = 24
Subject.teacher = "Marley"
"""print(biology.students)
print(math.teacher)
print(math.__dict__)
print(biology.__dict__)
print("\n")
print(Subject.__dict__)
"""
#print(getattr(math, "creditLoad", 1993))
"""
def func(n):
	return n ** 2

func.n = 3
print(func.n)
print(func(func.n))

"""
print(math.__accredited)