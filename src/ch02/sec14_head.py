# -*- coding: utf-8 -*-
import sys
import os

"""
head -nN hightemp.txt
"""

current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../dat/hightemp.txt")

def head(filename, n):
    with open(filename, 'r') as f:
        #.readlines()はファイル内の各行を要素とするリストを返す
        l = f.readlines()[:n]
        for e in l:
            print(e.rstrip('\n'))


if __name__ == '__main__':
    n = int(sys.argv[1])
    head(data, n)
