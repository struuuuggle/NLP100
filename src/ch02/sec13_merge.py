# -*- coding: utf-8 -*-

def merge(col1_filename,col2_filename):
    f1, f2 = open(col1_filename, 'r'), open(col2_filename, 'r')
    f3 = open('./test/sec13.txt', 'a')
    for w1, w2 in zip(f1.read().split('\n'), f2.read().split('\n')):
        f3.write(w1  + '\t' + w2 + '\n')
    f1.close(), f2.close(), f3.close()

def main():
    col1_filename, col2_filename = './test/col1.txt', './test/col2.txt'
    merge(col1_filename, col2_filename)

if __name__ == '__main__':
    main()
