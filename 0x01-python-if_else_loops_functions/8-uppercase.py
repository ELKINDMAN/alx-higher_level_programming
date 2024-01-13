#!/usr/bin/python3
def uppercase(str):
    for _char in str:
        asval = ord(_char)
        if 97 <= asval <= 122:
            asval -= 32
        print("{}".format(chr(asval)), end='')
    print()
