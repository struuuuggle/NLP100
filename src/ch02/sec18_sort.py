# -*- coding: utf-8 -*-
import pandas as pd

def sort(filename):
    df = pd.read_table(filename, names=('A', 'B', 'C', 'D'))
    df_s = df.sort_values(by='C')
    df_s.to_csv('./test/sec18.txt', header=None, index=False, sep='\t')

def main():
    filename = '../../lib/hightemp.txt'
    sort(filename)

if __name__ == '__main__':
    main()
