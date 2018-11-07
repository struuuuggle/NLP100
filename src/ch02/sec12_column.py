# -*- coding: utf-8 -*-
import os

"""
cut -f 1 hightemp.txt #hightemp.txtの1列目だけを抜き出す
cut -f 2 hightemp.txt #hightemp.txtの2列目だけを抜き出す
"""

DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH = os.path.join(DIR, "../../dat/hightemp.txt")
COL1_PATH = os.path.join(DIR, "./test/col1.txt")
COL2_PATH = os.path.join(DIR, "./test/col2.txt")

# import numpy as np
# def divide(path=IN_PATH):
#     """
#     1列目をcol1.txtに，2列目をcol2.txtに保存
#     """
#     data = np.genfromtxt(path,
#                          dtype=[('col1', 'U16'), ('col2', 'U16'), ('col3', 'f'), ('col4', 'U16')],
#                          delimiter='\t')
#     with open(COL1_PATH, 'w') as f1, open(COL2_PATH, 'w') as f2:
#         l1, l2 = [], []
#         for tp in data:
#             l1.append(tp[0] + '\n'), l2.append(tp[1] + '\n')
#         f1.write(''.join(l1)), f2.write(''.join(l2))

def divide2(path=IN_PATH):
    col1, col2 = [], []
    for line in open(IN_PATH):
        col1.append(line.split('\t')[0])
        col2.append(line.split('\t')[1])


if __name__ == '__main__':
    # divide()
    divide2()
