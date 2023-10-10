#!/usr/bin/python3
""" This module supplies one funciton """
import json


def save_to_json_file(my_obj, filename):
    """  writes an Object to a text file, using a JSON representation """
    text = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(text)
