# -*- coding: utf-8 -*-
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
col1 = os.path.join(current_dir, "./test/col1.txt")
col2 = os.path.join(current_dir, "./test/col2.txt")
output = os.path.join(current_dir, "./test/merged.txt")

def merge(col1, col2):
    lst = []
    with open(col1, 'r') as col1f, open(col2, 'r') as col2f:
        for line1, line2 in zip(col1f, col2f):
            lst.append(line1.rstrip('\n') + '\t' + line2.rstrip('\n'))

    with open(output, 'w') as f:
        for element in lst:
            f.write(element + '\n')

def main():
    merge(col1, col2)

if __name__ == '__main__':
    main()
