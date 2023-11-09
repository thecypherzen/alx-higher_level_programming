#include "Python.h"
#include <stdio.h>
#include <sys/types.h>
#include "bytesobject.h"
#include "object.h"

/**
 * print_python_bytes - prints bytes of a python object
 * @p: ptr to python object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	int is_bytes = PyBytes_Check(p);
	PyBytesObject *obj;
	Py_ssize_t objsize, max_len, i;

	if (!is_bytes)
		printf("[ERROR] Invalid Bytes Object\n");
	else
	{
		obj = (PyBytesObject *)p;
		objsize = obj->ob_base.ob_size;
		printf("[.] bytes object info\n");
		printf(" size: %ld\n", objsize);
		printf(" trying string: %s\n", obj->ob_sval);
		max_len = objsize + 1 <= 10 ? objsize + 1 : 10;
		printf(" first %lu bytes:", max_len);
		for (i = 0; i < max_len; i++)
			printf("  %02x", (unsigned char)obj->ob_sval[i]);
		printf("\n");
	}
}


/**
 * print_python_list - prints info of a python list
 * @p: pointer to python list object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyListObject *listobj = (PyListObject *)p;
	Py_ssize_t list_sz = listobj->ob_base.ob_size, i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = 2: %ld\n", list_sz);
	printf("[*] Allocated: %ld\n", listobj->allocated);
	for (i = 0; i < list_sz; i++)
		printf("Element: %ld, %s\n", i, listobj->ob_item[i]->ob_type->tp_name);
}
