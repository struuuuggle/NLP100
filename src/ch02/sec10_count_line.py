# -*- coding: utf-8 -*-

"""
wc -l hightemp.txt
"""
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../dat/hightemp.txt")

def count_line(filename):
    with open(filename, 'r') as f:
        return len(f.read().rstrip('\n').split('\n'))

if __name__ == '__main__':
    print(count_line(data))
