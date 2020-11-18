/* 
special implemenation of deque using array in C with C/C++ extension modules for CPython

07/24/20, Peiheng Li (jdlph@hotmail.com)
*/


#include <Python.h>
#include <structmember.h>

typedef struct {
    PyObject_HEAD
    int *elem;
    int head;
    int tail;
} DequeC;

static PyObject *
DequeC_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    DequeC *self;
    self = (DequeC *)type->tp_alloc(type, 0);
    if (self==NULL)
        return NULL;

    return (PyObject *) self;
}

static int
DequeC_init(DequeC *self, PyObject *args, PyObject *kwds)
{
    int size_;
    if (!PyArg_ParseTuple(args, "i", &size_))
        return NULL;

    self->elem = (int *)malloc(sizeof(int)*size_);
    self->head = -1;
    self->tail = -1;

    return 0;
}

static PyObject *
DequeC_appendleft(DequeC *self, PyObject *nodeID)
{
    int nodeID_ = _PyLong_AsInt(nodeID);
    if (self->head==-1)
    {
        self->elem[nodeID_] = -1;
        self->head = nodeID_;
        self->tail = nodeID_;
    }
    else
    {
        self->elem[nodeID_] = self->head;
        self->head = nodeID_;
    }
    Py_RETURN_NONE;
}

static PyObject *
DequeC_append(DequeC *self, PyObject *nodeID)
{
    int nodeID_ = PyLong_AsLong(nodeID);
    if (self->head==-1)
    {
        self->head = nodeID_;
        self->tail = nodeID_;
        self->elem[nodeID_] = -1;
    }
    else
    {
        self->elem[self->tail] = nodeID_;
        self->elem[nodeID_] = -1;
        self->tail = nodeID_;
    }
    Py_RETURN_NONE;
}

static PyObject *
DequeC_popleft(DequeC *self)
{
    int left_ = self->head;
    self->head = self->elem[left_];
    self->elem[left_] = -1;
    return PyLong_FromLong(left_);
}

static int
DequeC_bool(DequeC *self)
{
    return self->head != -1;
}

static PyObject *
DequeC_clear(DequeC *self)
{
    self->head = -1;
    self->tail = -1;
    Py_RETURN_NONE;
}

static void
DequeC_dealloc(DequeC *self)
{
    Py_TYPE(self)->tp_free((PyObject *)self);
}

static PyNumberMethods DequeC_as_number = {
    0,                                  /* nb_add */
    0,                                  /* nb_subtract */
    0,                                  /* nb_multiply */
    0,                                  /* nb_remainder */
    0,                                  /* nb_divmod */
    0,                                  /* nb_power */
    0,                                  /* nb_negative */
    0,                                  /* nb_positive */
    0,                                  /* nb_absolute */
    (inquiry)DequeC_bool,               /* nb_bool */
    0,                                  /* nb_invert */
 };

static PyMethodDef DequeC_methods[] = {
    {"append", (PyCFunction)DequeC_append, METH_O, "append a new node from back"},
    {"appendleft", (PyCFunction)DequeC_appendleft, METH_O, "append a new node from front"},
    {"popleft", (PyCFunction)DequeC_popleft, METH_NOARGS, "pop the first node in DequeC and return its index"},
    {"clear", (PyCFunction)DequeC_clear, METH_NOARGS, "clear the DequeC for new use but not release the memory"},
    {"dealloc", (PyCFunction)DequeC_dealloc, METH_NOARGS, "destruct the DequeC object and release the momory"},
    {NULL} /* Sentinel */
};

static PyTypeObject ClassyType = {
    PyVarObject_HEAD_INIT(NULL, 0) 
    "DequeC",                                 /* tp_name */
    sizeof(DequeC),                           /* tp_basicsize */
    0,                                        /* tp_itemsize */
    (destructor)DequeC_dealloc,               /* tp_dealloc */
    0,                                        /* tp_print */
    0,                                        /* tp_getattr */
    0,                                        /* tp_setattr */
    0,                                        /* tp_reserved */
    0,                                        /* tp_repr */
    &DequeC_as_number,                        /* tp_as_number */
    0,                                        /* tp_as_sequence */
    0,                                        /* tp_as_mapping */
    0,                                        /* tp_hash  */
    0,                                        /* tp_call */
    0,                                        /* tp_str */
    0,                                        /* tp_getattro */
    0,                                        /* tp_setattro */
    0,                                        /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags */
    "Simple DequeC using Array",              /* tp_doc */
    0,                                        /* tp_traverse */
    0,                                        /* tp_clear */
    0,                                        /* tp_richcompare */
    0,                                        /* tp_weaklistoffset */
    0,                                        /* tp_iter */
    0,                                        /* tp_iternext */
    DequeC_methods,                           /* tp_methods */
    0,                                        /* tp_members */
    0,                                        /* tp_getset */
    0,                                        /* tp_base */
    0,                                        /* tp_dict */
    0,                                        /* tp_descr_get */
    0,                                        /* tp_descr_set */
    0,                                        /* tp_dictoffset */
    (initproc)DequeC_init,                    /* tp_init */
    0,                                        /* tp_alloc */
    DequeC_new,                               /* tp_new */
};

/* this defines the module name, which should match the one in setup.py */
static struct PyModuleDef SimpleDequeCmodule = {
    PyModuleDef_HEAD_INIT,
    "SimpleDequeC",
    "SimpleDeque module containing DequeC class",
    -1,
    DequeC_methods,
    NULL,
};

PyMODINIT_FUNC PyInit_SimpleDequeC(void) {
    PyObject *m;
    if (PyType_Ready(&ClassyType) < 0)
        return NULL;

    m = PyModule_Create(&SimpleDequeCmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&ClassyType);
    if (PyModule_AddObject(m, "deque", (PyObject *) &ClassyType) < 0) {
        Py_DECREF(&ClassyType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}