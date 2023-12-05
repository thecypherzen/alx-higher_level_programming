#!/usr/bin/python3
size = 53

def add_digits(num):
	div = 1
	sum = 0
	while (num // div) > 9:
		div *= 10
	while div > 1:
		sum += (num // div) % 10
		num = num % div
		div //= 10
	sum += num
	print(sum)
	return sum

def get_hash(key):
	global size
	if not isinstance(key, str):
		raise TypeError("key must be a string type")
	k = 31
	hash = 0
	for i in range(len(key)):
		hash = (k * hash) + ord(key[i])
		hash = hash & 0x7fffffff
	return hash % size
