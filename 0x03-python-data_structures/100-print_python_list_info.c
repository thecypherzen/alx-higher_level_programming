#include "Python.h"
#include <stdio.h>
#include <sys/types.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info of a python list
 * @p: pointer to python list object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = list->ob_base.ob_size, i;

	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
		printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
}
