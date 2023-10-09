#!/usr/bin/python3
""" There's one class in this module """


class MyList(list):

    """ prints the list, but sorted (ascending sort) """
    def print_sorted(self):
        print(sorted(self))
