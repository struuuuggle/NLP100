# -*- coding: utf-8 -*-
import sys

def head(file, n):
    ln = 0
    for l in file:
        print(l, end='')
        ln += 1
        if ln == n:
            break
    return

def main():
    n = int(sys.argv[1])
    file = open('../src/hightemp.txt', 'r')
    head(file, n)

if __name__ == '__main__':
    main()
