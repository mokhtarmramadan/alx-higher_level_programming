#!/usr/bin/python3
""" This module supplies one functions """
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file” """
    with open(filename, 'r') as file:
        return json.load(file)
