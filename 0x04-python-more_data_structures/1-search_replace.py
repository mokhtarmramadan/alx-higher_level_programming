#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index = 0
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list[i] = replace
        else:
            continue
    return new_list
