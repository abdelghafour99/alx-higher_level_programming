#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints
 *			    info about a python list
 * @p: PyObject
 */

void print_python_list_info(PyObject *p)
{
	long int s, a;
	PyListObject *py_list;
	PyObject *itm;

	s = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", s);

	py_list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", py_list->allocated);

	for (a = 0; a < size; a++)
	{
		itm = PyList_GetItem(p, a);
		printf("Element %ld: %s\n", a, Py_TYPE(itm)->tp_name);
	}
}
