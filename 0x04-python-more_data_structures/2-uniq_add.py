#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = set(my_list)
    result = 0
    for item in uni:
        result += item
    return result
