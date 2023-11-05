#!/usr/bin/python3

"""
def name_demo(i, *args, **kwargs):
    for arg in args:
        i += 1
        print(f"arg {i}: {arg}")
    print("-" * 50)
    for kw in kwargs:
        print(f"{kw}: {kwargs[kw]}")

name_demo("free", "fall","to", age=30, name="maestro", city="bigi")
"""

"""
def funcs_flag_demo(count, *, arg1, arg2):
    for i in range(count):
        print(f"{i + 1} <=> arg1: {arg1}, arg2: {arg2}")


funcs_flag_demo(5, "arg10", "arg9")
"""
"""
def makepath(*args, sep="/"):
    new = sep.join(args)
    print(new)

makepath("root", "home", "directory")

"""

"""
defl = [range(3, 10)]
mylist = list(*defl)
print(mylist)
"""

"""
#lambda Expressions

def auto_incrementor(start: int=0) -> function:
	#""Function doc

	I really don't understand what they are saying here
	""
	return lambda x : x + start

increase = auto_incrementor(5)
print(increase(1))
print(increase(5))
print(auto_incrementor.__doc__)
print(auto_incrementor.__annotations__)
"""