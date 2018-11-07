# -*- coding: utf-8 -*-
import sys
import os

"""
tail -nN hightemp.txt
"""

DIR = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(DIR, "../../dat/hightemp.txt")

def tail(path, n):
    with open(path, 'r') as f:
        l = f.readlines()[-n:]
        for e in l:
            print(e.rstrip('\n'))


if __name__ == '__main__':
    n = int(sys.argv[1])
    tail(TXT_PATH, n)
