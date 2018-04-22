# -*- coding: utf-8 -*-
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")

def head(filename, n):
    with open(filename, 'r') as f:
        #.readlines()はファイル内の各行を要素とするlリストを返す
        lst = f.readlines()[:n]
        for e in lst:
            print(e.rstrip('\n'))

def main():
    n = int(sys.argv[1])
    head(data, n)

if __name__ == '__main__':
    main()
