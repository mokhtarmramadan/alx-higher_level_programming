#!/usr/bin/python3
flage = False
for i in range(122, 96, -1):
    if not flage:
        flage = True
        print(chr(i), end='')
    else:
        flage = False
        print(chr(i - 32), end='')
