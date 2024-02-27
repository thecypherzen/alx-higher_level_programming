#!/usr/bin/python3
"""0x0B. Python - Input/Output - Task 7

A script that adds all arguments to a Python list,
    and then saves them to a file:

    - If file already exists, it updates the list, if it doesn't
        exist, it is created.
    - filename must be ``add_item.json``
    - the file must be json
"""
import os
import sys

from_json_f = __import__("6-load_from_json_file").load_from_json_file
to_json_f = __import__("5-save_to_json_file").save_to_json_file

if os.path.exists("add_item.json"):
    listobj = from_json_f("add_item.json")
else:
    listobj = []

# add args to list
argc = len(sys.argv)
for i in range(1, argc):
    listobj.append(sys.argv[i])

# dump list to file
to_json_f(listobj, "add_item.json")
