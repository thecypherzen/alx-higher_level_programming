#!/usr/bin/python3

def uniq_add(my_list=[]):
	"""A function that adds all unique integers in a list
	(only once for each integer).

	Parameters:
		@my_list: the list of integers

	Return:
		Sum of unique integers

	Notes:
		- No imports allowed
	"""
	sum = 0
	if not my_list:
		return sum
	for i in set(my_list):
		sum += i if type(i) is int  else 0
	return sum


my_list = [1, 2, 3, 1, 4, 2, 5, "rex"]
result = uniq_add(None)
print(result)
print("Result: {:d}".format(result))
