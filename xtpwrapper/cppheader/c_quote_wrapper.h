

#ifndef C_QUOTE_WRAPPER
#define C_QUOTE_WRAPPER

#include "Python.h"
#include "pythread.h"
#include "xtp_quote_api.h"

#define Python_GIL(func) \
	do { \
		PyGILState_STATE gil_state = PyGILState_Ensure(); \
		if ((func) == -1) PyErr_Print();  \
		PyGILState_Release(gil_state); \
	} while (false)



#endif /* CMDAPI_H */