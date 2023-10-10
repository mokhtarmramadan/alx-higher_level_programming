#!/usr/bin/python3
""" This module supplies one fucntion """
import json


def to_json_string(my_obj):
    """ returns a JSON representation of an object """
    return json.dumps(my_obj)
