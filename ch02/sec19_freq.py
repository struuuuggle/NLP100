# -*- coding: utf-8 -*-
import pandas as pd
from collections import Counter

def freq(filename):
    df = pd.read_table(filename, names=('A', 'B', 'C', 'D'))
    common = Counter([x for x in df['A']]).most_common()
    return common

def main():
    filename = '../src/hightemp.txt'
    print(freq(filename))

if __name__ == '__main__':
    main()
