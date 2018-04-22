# -*- coding: utf-8 -*-
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")

def count_line(filename):
    f = open(filename, 'r')
    sum = 0
    for x in f:
        sum += 1
    return sum

def main():
    print(count_line(data))

if __name__ == '__main__':
    main()
