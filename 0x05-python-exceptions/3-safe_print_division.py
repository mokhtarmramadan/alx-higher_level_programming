#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        b = a / b
    except ZeroDivisionError:
        b = None
    finally:
        print("Inside result: {}".format(b))
        return b
