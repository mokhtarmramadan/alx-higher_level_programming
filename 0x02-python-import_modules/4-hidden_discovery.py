#!/usr/bin/python3

if __name__ == '__main__':
    import hidden_4

    all_names = dir(hidden_4)

    for name in all_names:
        if name[:2] == "__":
            continue
        else:
            print(name)
