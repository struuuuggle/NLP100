# -*- coding: utf-8 -*-
import sys

def head1(filename, n):
    file = open(filename, 'r')
    ln = 0
    for l in file:
        print(l, end='')
        ln += 1
        if ln == n:
            break
    return

def head2(filename, n):
    file = open(filename, 'r')
    #.readlines()はファイル内の各行を要素とするlリストを返す
    buf = file.readlines()[:n]
    print(''.join(buf), end='')
    return

def main():
    n = int(sys.argv[1])
    filename = '../src/hightemp.txt'
    #head1(filename, n)
    head2(filename, n)

if __name__ == '__main__':
    main()
