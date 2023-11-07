#include <stdio.h>
#include "Python.h"
#include <time.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
}