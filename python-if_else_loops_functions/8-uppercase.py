#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in "{}".format(str):
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        result += c
    print("{}".format(result))
