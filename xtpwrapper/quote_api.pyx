from cpython cimport PyObject
from libc.stdlib cimport malloc, free
from libc.string cimport const_char
from libcpp cimport bool as cbool


from .headers.xtp cimport