#!/usr/bin/python3

def add_integer(a, b=98):
	if any(i is None for i in (a, b)) \
		or any(not isinstance(i, int) and not isinstance(i, float) \
		 		for i in (a, b)):
		raise TypeError("a must be an integer or b must be an integer")
	res = int(a) + int(b)
	return res
