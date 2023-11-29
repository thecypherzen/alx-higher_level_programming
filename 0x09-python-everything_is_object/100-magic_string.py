#!/usr/bin/python3
def magic_string(count=0):
	count += 1
	return "BestSchool" * count


for i in range(10):
	print(magic_string())