#!/usr/bin/python3
#import os
import sys
from io import StringIO

#file = open("./myfile.tx", "a+")
#file.seek(0)
#i = 0
#file.write("line five\n")
#for line in file.readlines():
#	i += 1
#	print(f"line: {i}: {line}", end="")
#file.close()
#if os.path.exists("./myfile.tx"):
#	#os.remove("./myfile.tx")

myfile = StringIO()
sys.stdout = myfile
print("This was redirected from stdout")
myfile.seek(0)
sys.stdout = sys.__stdout__
print(myfile.read(), end="")
