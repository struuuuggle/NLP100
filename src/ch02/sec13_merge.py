# -*- coding: utf-8 -*-
import os

"""
paste -d '\t' col1.txt col2.txt
"""

DIR = os.path.dirname(os.path.abspath(__file__))
COL1_PATH = os.path.join(DIR, "./test/col1.txt")
COL2_PATH = os.path.join(DIR, "./test/col2.txt")
OUT_PATH = os.path.join(DIR, "./test/sec13_merged.txt")

def merge(path1=COL1_PATH, path2=COL2_PATH, path3=OUT_PATH):
    l = []
    with open(path1, 'r') as f1, open(path2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            l.append(line1.rstrip('\n') + '\t' + line2.rstrip('\n'))

    with open(path3, 'w') as f:
        for element in l:
            f.write(element + '\n')


if __name__ == '__main__':
    merge()
