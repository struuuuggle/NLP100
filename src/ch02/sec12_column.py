# -*- coding: utf-8 -*-
import os
import numpy as np
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")
col1 = os.path.join(current_dir, "./test/col1.txt")
col2 = os.path.join(current_dir, "./test/col2.txt")

# divideとかに改名したい
def column(src):
    """
    1列目をcol1.txtに，2列目をcol2.txtに保存
    """
    data = np.genfromtxt(src,
                         dtype=[('col1', 'U16'), ('col2', 'U16'), ('col3', 'f'), ('col4', 'U16')],
                         delimiter='\t')
    with open(col1, 'w') as col1_file, open(col2, 'w') as col2_file:
        l1, l2 = [], []
        for tp in data:
            l1.append(tp[0] + '\n'), l2.append(tp[1] + '\n')
        col1_file.write(''.join(l1)), col2_file.write(''.join(l2))

def main():
    column(data)

if __name__ == '__main__':
    main()
