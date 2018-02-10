# -*- coding: utf-8 -*-

def count_line(filename):
    f = open(filename, 'r')
    sum = 0
    for x in f:
        sum += 1
    return sum

def main():
    filename = '../src/hightemp.txt'
    print(count_line(filename))

if __name__ == '__main__':
    main()
