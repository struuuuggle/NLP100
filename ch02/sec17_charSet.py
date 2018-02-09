# -*- coding: utf-8 -*-
import pandas as pd

def charSet(filename):
    df = pd.read_table(filename, names=('A', 'B', 'C', 'D'))
    s1 = set([x for x in df['A']])
    return s1

def main():
    filename = '../src/hightemp.txt'
    print(charSet(filename))

if __name__ == '__main__':
    main()
