#!/usr/bin/python3


# Task 10
""" Check """
import inspect

square_import = __import__('models.square').square

if square_import is None:
    print("Can't import models.square")
    exit(1)

square_class = square_import.__dict__.get('Square')
if square_class is None:
    print("Can't find class Square in models.square")
    exit(1)
print(square_class)

if not inspect.isclass(square_class):
    print("Square is not a class")
    exit(1)

from models.rectangle import Rectangle

print(Rectangle)

if not issubclass(square_class, Rectangle):
    print("Square is not a subclass of Rectangle")
    exit(1)

print("OK", end="")


# Task 17 or so
#""" Check """
#from models.square import Square
#from models.rectangle import Rectangle
#from models.base import Base
#import json
#import uuid
#import random

#list_dictionaries = []
#map_dictionaries = {}
#for i in range(0, 5):
#    r = Rectangle(random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2))
#    rd = r.to_dictionary()
#    list_dictionaries.append(rd)
#    map_dictionaries[r.id] = rd

#    s = Square(random.randrange(1, 100, 2), random.randrange(1, 100, 2), random.randrange(1, 100, 2))
#    sd = s.to_dictionary()
#    list_dictionaries.append(sd)
#    map_dictionaries[s.id] = sd

#for i in range(0, 5):
#    rd = { 'id': (len(list_dictionaries) + 10), 'name': str(uuid.uuid4()) }
#    list_dictionaries.append(rd)
#    map_dictionaries[rd.get('id')] = rd


#rjson = Base.to_json_string(list_dictionaries)
#output_list = json.loads(rjson)

#for output in output_list:
#    id_output = output.get('id')
#    if id_output is None:
#        break
#    dict_output = map_dictionaries.get(id_output)
#    if dict_output is None:
#        break
#    if dict_output != output:
#        break
#    del map_dictionaries[id_output]

#if len(map_dictionaries) != 0:
#    print("to_json_string doesn't correctly serialize {}: {}".format(list_dictionaries, rjson))
#    exit(1)
#print(map_dictionaries)
#print("OK", end="")