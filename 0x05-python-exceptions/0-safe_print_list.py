#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 1
    for i in range(x):
        try:
            print(my_list[i], end='')
        except IndexError:
            counter -= 1
            pass
    counter += i
    print()
    return counter
