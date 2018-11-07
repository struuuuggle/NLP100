# -*- coding: utf-8 -*-
import os
import pandas as pd
from collections import Counter

DIR = os.path.dirname(os.path.abspath(__file__))
TXT_PATH = os.path.join(DIR, "../../dat/hightemp.txt")

def freq(path=TXT_PATH):
    df = pd.read_table(path, names=('col1', 'col2', 'col3', 'col4'))
    sorted_data = Counter([x for x in df['col1']]).most_common()
    return sorted_data


if __name__ == '__main__':
    for item in freq():
        print(f'{item[0]}: {item[1]}回')
