# -*- coding: utf-8 -*-
import sys
from sec10_count_line import count_line

def split(filename, n):
    """
    fileをn分割して、div行ずつn個のファイルにそれぞれ書き込む
    """
    src_f = open(filename, 'r')
    src_list = src_f.read().split('\n')
    div = int(countRow(filename) / n)
    for i in range(n):
        out_f = open(('./test/sec16_xa' + chr(ord('a') + i) + '.txt'), 'w')
        out_f.write('\n'.join(src_list[div*i:div*(i+1)]))
        out_f.close()
    src_f.close()

def main():
    filename = '../../lib/hightemp.txt'
    n = int(sys.argv[1])
    split(filename, n)

if __name__ == '__main__':
    main()
