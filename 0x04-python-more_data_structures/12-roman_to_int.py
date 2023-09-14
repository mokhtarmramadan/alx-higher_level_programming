#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
    sum = 0
    prev = 0

    if not roman_string or not isinstance(roman_string, str):
        return 0

    for num in roman_string:
        if romans[num] > prev and prev != 0:
            sum += (-2 * prev) + romans[num]
            prev = romans[num]
        elif prev == 0:
            sum = romans[num]
            prev = romans[num]
        else:
            sum += romans[num]
            prev = romans[num]

    return abs(sum)
