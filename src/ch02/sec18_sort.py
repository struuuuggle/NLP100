# -*- coding: utf-8 -*-
import os
import pandas as pd
DIR = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(DIR, "../../dat/hightemp.txt")

def sort(path=TXT_PATH):
    df = pd.read_table(path, names=('col1', 'col2', 'col3', 'col4'))
    df_s = df.sort_values(by='col3')
    df_s.to_csv('./test/sec18.txt', header=None, index=False, sep='\t')


if __name__ == '__main__':
    sort()
