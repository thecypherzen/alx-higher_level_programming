#include <stdio.h>
#include <time.h>
#include "Python.h"

/**
 * print_python_list_info - prints info of a python list
 * @p: pointer to python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
}
