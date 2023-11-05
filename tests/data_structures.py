#!/usr/bin/python3

"""
#List Methods
mylist = list(range(1, 3))
print(mylist)
mylist.insert(len(mylist), 3)
print(mylist)
mylist.extend(range(5, 8))
print(mylist)
mylist.insert(0, -1)
print(mylist)
i = mylist.index(3, 0, 4)
print(f"{mylist[i]} is at index {i}")
print(f"number of {2}s in mylist: {mylist.count(2)}")
mylist.reverse()
print(f"reversed: {mylist}")
"""


#List Comprehensions
"""
odds20 = [x for x in range(21) if x % 2]
squares10 = list(map(lambda x: x ** 2, range(1, 11)))
print(odds20)
print(squares10)
"""

"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
#one way of tranposing
#transposed = []
#for i in range(len(matrix[0])):
#	transposed.append([j[i] for j in matrix])
#print(transposed)

# Another way
###transposed = [[row[i] for row in matrix] for i in range(4)]
##print(transposed)

# Using zip()
transposed = list(zip(*matrix))
print(transposed)
listid = id(transposed)
print(f"address of list: {listid:<15}\tHex: {hex(listid):<15}")
"""
"""
alpha = {'fname': "johnson", "lname": "Jumapia"}
for key, val in alpha.items():
    print(f"key: {key}\tvalue: {val}")
"""
"""
import sys, builtins
import os
from glob import glob

args = sys.argv
len = len(args)
for i in range(1, len):
    print(args[i])
path = sys.path
path.append("./this/that")
#print(path)
#print("")
#print(dir(builtins))

print(os.getcwd())
dirfiles = glob("*.py")
print(dirfiles)
"""

# mylist = [-1, 1, 66.25, 333, 333, 1234.5]
# print(f"\nList: {mylist}")

# d = len(mylist)
# print("length: {}".format(d))

# print("\nDeleting d from stack & data")
# del d
# try:
#     print("len(mylist): {}".format(d))
# except NameError:
#     print("\nAccessing 'd' after deletion raises an exception")
#     print(NameError)
#     print("\nUntil we assign 'd' to another value.")
#     d = "some new value"
#     print(d)
#     print("\n")
# print("\nidx = mylist.index(333)")
# idx = mylist.index(333)
# print(f"returned val: {idx}\n")

# print("\nidx = mylist.index(333, 4)")
# idx = mylist.index(333, 4)
# print(f"returned val: {idx}\n")

# print("\nidx = mylist.index(300)")
# idx = mylist.index(300)
# print(f"returned val: {idx}\n")

# mylist = [27, 19, 12, -3, 4, -12, -18, 102, 98, 27.3, -18.24]
# print(f"\nList: {mylist}")

# n = 333
# count = mylist.count(333)
# print(f"{n} appears {count} times in mylist\n")
# n = -3
# count = mylist.count(-3)
# print(f"{n} appears {count} times in mylist\n")
# def last_digit(n):
# 	return abs(n) % 10

# mylist = [27, 19, 12, -3, 4, -12, -18, 102, 98, 27.3, -18.24]
# print(f"\nList: {mylist}")

# print("\nsorting only with mylist.sort():")
# mylist.sort()
# print(mylist)

# mylist = [27, 19, 12, -3, 4, -12, -18, 102, 98, 27.3, -18.24]
# print("\nsorting and reversing at same time:")
# mylist.sort(reverse=True)
# print(mylist)

# print("\ncan also use lambda expression as key")
# mylist = [27, 19, 12, -3, 4, -12, -18, 102, 98, 27.3, -18.24]
# print(f"Original List: {mylist}\n")
# print("mylist.sort(key=lambda x: abs(x) % 10, reverse=True)")
# mylist.sort(key=lambda x: abs(x) % 10)
# print(mylist)
# print("\n")


# mylist = [-18, 102, 98, 27.3, -100]
# mylistcpy = deepcopy(mylist)

# print(f"\nmylist: {mylist}")
# print(f"id of mylist:{id(mylist)}")

# print(f"\nmylistcpy: {mylistcpy}")
# print(f"id of mylistcpy:{id(mylistcpy)}\n")

# print(f"\nmylist is mylistcpy: {mylist is mylistcpy}")
# print(f"mylist[0] is mylistcpy[0]: {mylist[0] is mylistcpy[0]}")

# mylist[0] = 988
# print(f"\nmylist: {mylist}")
# print(f"mylistcpy: {mylistcpy}")
# print("\n")

# from copy import deepcopy

# mylist = [[10, 24], [-2, 3, 9, 20]]
# mylistcpy = deepcopy(mylist)

# print("\nBefore mutation:")
# print(f"mylist:{mylist}\nmylistcpy: {mylistcpy}")
# mylist[0][0] = 1024
# mylistcpy[1][3] = 133

# print("\nAfter mutation:")
# print(f"mylist:{mylist}\nmylistcpy: {mylistcpy}")
# print("\n")

# PRACTICING THE POP, APPEND AND INSERT - USING LISTS AS A QUEUE
# OR STACK
# mylist = [[10, 24], [-2, 3, 9, 20]]
# print(mylist)
# one = mylist.pop()
# print(one)
# print (mylist)

# mylist.append(99)
# mylist.insert(1, 84)
# mylist.insert(0, 13)
# print(mylist)

# del mylist[0]
# print(mylist)


#USING COLLECTIONS.DEQUEUE
# from collections import deque
# from timeit import timeit

# # Creating the list and deque
# mylist = ['a', '3', 'name', 'ham', '14', 'joe']
# mydeque = deque(mylist)

# # function that deletes from and inserts to left of list
# def l_deque(mylist: list) -> None:
#     del mylist[0]
#     mylist.insert(0, 55)

# # a function that pops from and inserts to left of a deque
# def q_deque(mydeque: deque) -> None:
#     mydeque.popleft()
#     mydeque.insert(0, 55)

# print(f"\nBefore:\nList: {mylist}\nDeque: {mydeque}\n")

# # timing the functions
# ldeque_time = timeit(stmt='l_deque(mylist)',
#                      globals=globals(), number=5)
# qdeque_time = timeit(stmt='q_deque(mydeque)',
#                      globals=globals(), number=5)
# tlist = round((ldeque_time * 1000000), 2)
# tdeque = round((qdeque_time * 1000000), 2)

# # timing results
# print(f"time for list: {tlist}")
# print(f"time for queue: {tdeque}")
# print(f"diff: (list - deque): {round((tlist - tdeque), 2)}")

# print(f"\nAfter:\nList:{mylist}\nDeque: {mydeque}\n")

#tuples
tpl1 = 'this', 3, 4.9, "that"
print(tpl1[2])
tpl2 = tpl1, 'second', 'minute'
print(*tpl2[1])
