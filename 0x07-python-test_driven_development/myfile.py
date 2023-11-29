#!/usr/bin/python3

import sys
from io import StringIO

wstream = open("iostream", "w")
rstream = open("iostream", "r")

sys.stdout = wstream
print("Line1\nLine2\nLine3\n", end="")
wstream.truncate(0)
wstream.seek(0)
sys.stdout = sys.__stdout__

#if rstream.tell():
#    rstream.seek(0)
wstream.write("newline\n")
wstream.seek(0)

lines = rstream.readlines()
print(lines)
