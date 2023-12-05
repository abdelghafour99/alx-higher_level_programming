#include <stdio.h>
#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - function that prints
 *			    info about a python list
 * @p: PyObject
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *py_list = NULL;
	ssize_t len_list = 0;
	ssize_t a = 0;
	const char *el_type = NULL;

	len_list = PyList_Size(p);
	py_list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", len_list);
	printf("[*] Allocated = %ld\n", (signed long)(py_list->allocated));
	while (a < len_list)
	{
		el_type = Py_TYPE(py_list->ob_item[a])->tp_name;
		printf("Element %ld: %s\n", a, el_type);
		a++;
	}
}
