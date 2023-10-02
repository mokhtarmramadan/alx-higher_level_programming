#!/usr/bin/python3
def text_indentation(text):
    if text is None or not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_flag = False
    for char in text:
        if skip_flag:
            skip_flag = False
            continue
        if char in ['.', '?', ':']:
            print(char)
            print()
            skip_flag = True
        elif skip_flag is True and char == " ":
            pass
        else:
            print(char, end='')
