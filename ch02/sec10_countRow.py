# -*- coding: utf-8 -*-

def countRow(file):
    sum = 0
    for x in file:
        sum += 1
    return sum

def main():
    file = open('../src/hightemp.txt')
    print(countRow(file))

if __name__ == '__main__':
    main()
