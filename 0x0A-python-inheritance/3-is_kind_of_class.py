#!/usr/bin/python3
""" This module contians only one function """


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance or inherited from class """
    return isinstance(obj, a_class)
