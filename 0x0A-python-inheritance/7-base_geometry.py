#!/usr/bin/python3
""" This module supplies classes """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Public instance method: def area(self): """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if not isinstance(value, int) and type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
