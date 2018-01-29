# -*- coding: utf-8 -*-
import sys

def tail(file, n):
    buf = file.readlines()[-n:]
    print(''.join(buf), end='')
    return

def main():
    n = int(sys.argv[1])
    file = open('../src/hightemp.txt', 'r')
    tail(file, n)

if __name__ == '__main__':
    main()
