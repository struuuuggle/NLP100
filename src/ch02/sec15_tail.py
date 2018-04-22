# -*- coding: utf-8 -*-
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")

def tail(filename, n):
    with open(filename, 'r') as f:
        lst = f.readlines()[-n:]
        for e in lst:
            print(e.rstrip('\n'))

def main():
    n = int(sys.argv[1])
    tail(data, n)

if __name__ == '__main__':
    main()
