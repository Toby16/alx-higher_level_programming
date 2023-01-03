#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        if c in ord(i):
            return True
    for i in range(65, 91):
        if c in ord(i):
            return False
