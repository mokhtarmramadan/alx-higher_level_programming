#!/usr/bin/python3
""" This module dds all arguments to a Python list,
and then save them to a file """
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """ main - Entry point """
    try:
        obj = load_from_json_file('add_item.json')
        args = obj + argv[1:]
    except FileNotFoundError:
        args = argv[1:]
    save_to_json_file(args, 'add_item.json')


if __name__ == '__main__':
    main()
