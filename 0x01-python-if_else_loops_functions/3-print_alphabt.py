#!/usr/bin/python3
for current_char in range(ord('a'), ord('z') + 1):
    if chr(current_char) not in ('e', 'q'):
        print("{}".format(chr(current_char)), end='')
