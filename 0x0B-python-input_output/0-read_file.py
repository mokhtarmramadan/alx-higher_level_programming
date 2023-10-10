#!/usr/bin/python3
""" This module supplies one function """


def read_file(filename=""):
    """ reads file and prints it to the standerd output """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
