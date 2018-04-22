# -*- coding: utf-8 -*-
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")

from sec10_count_line import count_line

def split(filename, n):
    """
    入力ファイルをn分割してdiv行ずつ表示する
    """
    with open(filename, 'r') as f:
        lst = f.read().split('\n')
        div = int(count_line(filename) / n)
        for i in range(n):
            f = open(('./test/sec16_xa' + chr(ord('a') + i) + '.txt'), 'w')
            f.write('\n'.join(lst[div*i:div*(i+1)]))

def main():
    n = int(sys.argv[1])
    split(data, n)

if __name__ == '__main__':
    main()
