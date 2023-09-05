#!/usr/bin/python3
def main():

    flage = False
    for i in range(122, 96, -1):
        if not flage:
            flage = True
            print_rettel(i)
        else:
            flage = False
            print_rettel(i - 32)


def print_rettel(num):
    print(chr(num), end='')


if __name__ == "__main__":
    main()
