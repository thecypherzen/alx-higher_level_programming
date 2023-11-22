#include <sys/types.h>
#include "Python.h"
#include "object.h"
#include <stdio.h>

void print_python_list(PyObject *p)
{
	char *obj_type = p->ob_type->tp_name;

	setbuf(stdout, NULL);
	printf("%s\n", obj_type);
}
