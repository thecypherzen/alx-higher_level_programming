#!/usr/bin/python3
def m_func(a, b):
	"""Returns a * b
	works with text:
	>>> m_func("a", 3)
	'aaa'

	and numbers
	>>> m_func(9, 10)
	90

	but not if a and b are neither a float nor an int
	>>> try:
	...     m_func("2", "3")
	... except Exception as e:
	...     print(e)
	...
	one of a or b must be an int or float
	"""
	if all(not isinstance(i, int) and not isinstance(i, float)\
			for i in [a, b]):
		raise TypeError("one of a or b must be an int or float")
	return a * b


class Myobj:
	pass

def test_obj(object):
	"""Returns a list of an object's location
	>>> test_obj(Myobj()) #doctest: +ELLIPSIS
	[<doctests.Myobj object at 0x...>]
	"""
	return [object]
