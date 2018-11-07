# -*- coding: utf-8 -*-
import sys
import os
from sec10_count_line import count_line

"""
split -l N hightemp.txt
"""

DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(DIR, "../../dat/hightemp.txt")

def split(path, n):
    """
    入力ファイルをn分割してdiv行ずつ表示する
    """
    with open(path, 'r') as f:
        l = f.read().split('\n')
        div = int(count_line(path) / n)
        for i in range(n):
            f2 = open(('./test/sec16_xa' + chr(ord('a') + i) + '.txt'), 'w')
            print('\n'.join(l[div*i:div*(i+1)]))
            print('===')
            f2.write('\n'.join(l[div*i:div*(i+1)]))


if __name__ == '__main__':
    n = int(sys.argv[1])
    split(OUT_PATH, n)
