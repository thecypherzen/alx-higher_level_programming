#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 1.5
print("Element at index {} is {}".format(idx, element_at(my_list, idx)))
