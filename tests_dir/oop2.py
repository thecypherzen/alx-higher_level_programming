#!/usr/bin/python3
import datetime

class SchoolMember:
	def __init__(self, name, age, id):
		self.__name = name
		self.__age = age
		self.__id = id

	def info(self):
		print(f"My info: Name: {self.__name}, Age:{self.__age} ID: {self.__id}", end=" ")


class Student(SchoolMember):
	def __init__(self, name, age, id, course):
		SchoolMember.__init__(self, name, age, id)
		self.course = course



class Lecturer(SchoolMember):
	def __init__(self, name, age, id, qual, salary):
		SchoolMember.__init__(self, name, age, id)
		self.__qual = qual
		self.__salary = salary


st = Student("Larry Barry", 23, 2323, "Chemistry")
le = Lecturer("Antwam Jeremy", 32, 19193, "PGDE", 400000)

st.info()
le.info()