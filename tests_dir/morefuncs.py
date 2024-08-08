#!/usr/bin/python3
"""Task

- Create a function that receives a list and a function
- The function passed will return True or False if a list value is odd
- The surrounding function will return a list of odd numbers
"""
"""
ourList = [i for i in range (1, 21)]

def oddFunc(item):
	return True if item % 2 else False

def GetOddsList(mlist, func):
	ValList = [i for i in mlist if func(i) is True]
	return ValList

ourListofOdds = GetOddsList(ourList, oddFunc)

print(ourListofOdds)
"""
"""
def personinfo(name: str, age: int):
	try:
		return "{:s} is {:d} years old".format(name, age)
	except ValueError:
		return "Usage: personinfo(name: str, age: int)"

print(personinfo("Joshefa", 24))
print(personinfo("Gemade", 33))

"""
"""
mayday = {"one": "first item", "two": "second item"}

mkeys= mayday.keys()
mlist = [list(mkeys)]
print(type(mkeys))
print(type(mlist))
"""


# """Problem:

# 	- Create a random list filled with characters H and T for heads
# 		and tails and output the number of Heads and Tails.

# Example:
# 	Heads: 24
# 	Tails: 76
# """
# coinlist = []

# def getcoins(elist: list) -> str:
# 	import random
# 	coin = ('H', 'T')
# 	for i in range(100):
# 		elist.append(random.choice(coin))
# 	heads = elist.count('H')
# 	tails = elist.count('T')
# 	return "Heads: {}\nTails:{}".format(heads, tails)

# print(getcoins(coinlist))


"""Prolem:
	- Find the multiples of 9 from a random 100 value list
		with values from 1 to 1000
"""
def randone():
	import random
	myList = [random.choice(range(1000)) for i in range(100)]
	mult9 = list(filter(lambda x: not x % 9, myList))
	mult9.sort()
	return mult9

def randtwo():
	import random
	myList = [random.randint(0, 1000) for i in range(100)]
	mult9 = list(filter(lambda x: not x % 9, myList))
	mult9.sort()
	return mult9
print(randone())
print(randtwo())

import timeit
time1 = timeit.repeat(stmt='randone()', globals=globals(),
							number =12000, repeat=3)
time2 = timeit.repeat(stmt='randtwo()', globals=globals(),
							number=12000, repeat=3)
time1.sort()
time2.sort()
print("")
print("random.choice: {0}\nrandom.randint: {1}".format(round(time1[0], 2), round(time2[0], 2)))