# -*- coding: utf-8 -*-
import os
import pandas as pd
from collections import Counter
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")

def freq(filename):
    df = pd.read_table(filename, names=('col1', 'col2', 'col3', 'col4'))
    sorted_data = Counter([x for x in df['col1']]).most_common()
    return sorted_data

def main():
    print(freq(data))

if __name__ == '__main__':
    main()
