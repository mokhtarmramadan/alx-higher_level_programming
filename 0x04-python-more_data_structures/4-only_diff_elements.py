#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = list(set_1 - set_2) + list(set_2 - set_1)
    return diff_elements
