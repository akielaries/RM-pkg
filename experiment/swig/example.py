# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.0
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _example
else:
    import _example

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _example.delete_SwigPyIterator

    def value(self):
        return _example.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _example.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _example.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _example.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _example.SwigPyIterator_equal(self, x)

    def copy(self):
        return _example.SwigPyIterator_copy(self)

    def next(self):
        return _example.SwigPyIterator_next(self)

    def __next__(self):
        return _example.SwigPyIterator___next__(self)

    def previous(self):
        return _example.SwigPyIterator_previous(self)

    def advance(self, n):
        return _example.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _example.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _example.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _example.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _example.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _example.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _example.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _example:
_example.SwigPyIterator_swigregister(SwigPyIterator)

def new_std_mtx_add(nelements):
    return _example.new_std_mtx_add(nelements)

def delete_std_mtx_add(ary):
    return _example.delete_std_mtx_add(ary)

def std_mtx_add_getitem(ary, index):
    return _example.std_mtx_add_getitem(ary, index)

def std_mtx_add_setitem(ary, index, value):
    return _example.std_mtx_add_setitem(ary, index, value)
class MathOperations(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def add(self, *args):
        return _example.MathOperations_add(self, *args)

    def subtract(self, *args):
        return _example.MathOperations_subtract(self, *args)

    def multiply(self, *args):
        return _example.MathOperations_multiply(self, *args)

    def divide(self, *args):
        return _example.MathOperations_divide(self, *args)

    def std_mtx_add(self, *args):
        return _example.MathOperations_std_mtx_add(self, *args)

    def __init__(self):
        _example.MathOperations_swiginit(self, _example.new_MathOperations())
    __swig_destroy__ = _example.delete_MathOperations

# Register MathOperations in _example:
_example.MathOperations_swigregister(MathOperations)
