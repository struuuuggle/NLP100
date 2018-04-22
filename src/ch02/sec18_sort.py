# -*- coding: utf-8 -*-
import os
import pandas as pd
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")

def sort(filename):
    df = pd.read_table(filename, names=('col1', 'col2', 'col3', 'col4'))
    df_s = df.sort_values(by='col3')
    df_s.to_csv('./test/sec18.txt', header=None, index=False, sep='\t')

def main():
    sort(data)

if __name__ == '__main__':
    main()
