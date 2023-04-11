#!/usr/bin/python3
"""checks if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is an instance of a class
    or a class from which the class inherits
    """
    return (isinstance(obj, a_class))
