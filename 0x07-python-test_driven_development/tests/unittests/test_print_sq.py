#!/usr/bin/python3

print_square = __import__("4-print_square").print_square
from unittest import TestCase, main
import sys
istream = open("streamio", "r")
ostream = open("streamio", "w")

class TestPrintSquare(TestCase):
    # size is positive int
    def test_posint(self):
        sys.stdout = istream
        print_square(3)
        sys.stdout = sys.__stdout__
        lines = ostream.readlines().remove()
        self.assertEqual(len(lines), 4)
        for 
    
    # size is negative int
    # size is zero
    # size is float and > 0
    # size is float and < 0
    # size is float and is 0
    # size is float and Nan
    # size is float and neginf
    # size is float and posinf
    # size is None
    # size is str
        
