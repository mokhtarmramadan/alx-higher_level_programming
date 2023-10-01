#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not first_name or first_name is None or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if last_name is None or not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        print("My name is {:s}".format(first_name))
