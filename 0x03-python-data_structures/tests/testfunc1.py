#!/usr/bin/python3
import ctypes

func = ctypes.CDLL("./print_n.so")
print_n = func.print_n
print_n.argtypes = [ctypes.c_int]
print_n(20)