#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    value_list = list(a_dictionary.values())
    max_value = max(value_list)
    for k, v in a_dictionary.items():
        if v == max_value:
            return k
