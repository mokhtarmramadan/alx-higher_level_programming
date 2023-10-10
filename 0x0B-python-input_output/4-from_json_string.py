#!/usr/bin/python3
""" This module supplies one funciton """
import json


def from_json_string(my_str):
    """ returns an object represented by a JSON string """
    return json.loads(my_str)
