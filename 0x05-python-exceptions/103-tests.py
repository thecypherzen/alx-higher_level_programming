#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]

s = b"Hello"
lib.print_python_list(s)
