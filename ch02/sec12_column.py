# -*- coding: utf-8 -*-

def column(f_src, f_col1, f_col2):
    col1 = []
    col2 = []
    for line in f_src:
        cols = line.split('\t')
        col1.append(cols[0] + '\n')
        col2.append(cols[1] + '\n')
    f_col1.write(''.join(col1))
    f_col2.write(''.join(col2))
    return

def main():
    f_src = open('../src/hightemp.txt', 'r')
    f_col1 = open('../src/col1.txt', 'w')
    f_col2 = open('../src/col2.txt', 'w')
    column(f_src, f_col1, f_col2)

if __name__ == '__main__':
    main()
