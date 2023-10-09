#!/usr/bin/python3
""" This module contains one function """


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of the class """
    if type(obj) is a_class:
        return True
    return False
