# -*- coding: utf-8 -*-
import sys

def tail(filename, n):
    file = open(filename, 'r')
    buf = file.readlines()[-n:]
    print(''.join(buf), end='')
    return

def main():
    n = int(sys.argv[1])
    filename = '../../lib/hightemp.txt'
    tail(filename, n)

if __name__ == '__main__':
    main()
