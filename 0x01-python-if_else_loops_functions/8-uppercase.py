 #!/usr/bin/python3
def uppercase(str):
    str = str + '\n'
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print(i, end='')
