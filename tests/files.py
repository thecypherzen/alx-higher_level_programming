#!/usr/bin/python3
import os

file = open("./myfile.tx", "a+")
file.seek(0)
i = 0
file.write("line five\n")
for line in file.readlines():
	i += 1
	print(f"line: {i}: {line}", end="")
file.close()
if os.path.exists("./myfile.tx"):
	os.remove("./myfile.tx")