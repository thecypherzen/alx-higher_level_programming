#!/usr/bin/python3

def add(a, b):
	#if a < 0:
	#	a = (~a) + 1
	while b:
		c = a & b
		a = a ^ b
		b = c << 1
		print(f"a:{a} b: {b} b: {c}")
	return a

def mult(a, b):
	return (a << b)

def tobin(n):
	d = n >> 1
	i = 0
	while d:
		i += 1
		d >>= 1
	print("i: {}".format(i))
	while i:
		print(1 << i)
		i -= 1
	print(1 << i)

n = 6
tobin(n)