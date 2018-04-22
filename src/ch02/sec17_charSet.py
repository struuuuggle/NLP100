# -*- coding: utf-8 -*-
import os
import pandas as pd
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")

def charSet(filename):
    """
    1列目の文字列の種類（異なる文字列の集合）を求める
    """
    df = pd.read_table(filename, names=('col1', 'col2', 'col3', 'col4'))
    s1 = set([x for x in df['col1']])
    return s1

def main():
    print(charSet(data))

if __name__ == '__main__':
    main()
