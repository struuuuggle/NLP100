# -*- coding: utf-8 -*-
import os

"""
cut -f 1 hightemp.txt | sort | uniq
"""

DIR = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(DIR, "../../dat/hightemp.txt")

# import pandas as pd
# def charSet(filename):
#     """
#     1列目の文字列の種類（異なる文字列の集合）を求める
#     """
#     df = pd.read_table(filename, names=('col1', 'col2', 'col3', 'col4'))
#     s1 = set([x for x in df['col1']])
#     return s1

def charSet2(path=TXT_PATH):
    s1 = set([line.split('\t')[0] for line in open(path, 'r')])
    for i in s1:
        print(i)

if __name__ == '__main__':
    # print(charSet(TXT_PATH))
    charSet2()
