#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return (0, None)
    first_char = sentence[0]
    return (length, first_char)
