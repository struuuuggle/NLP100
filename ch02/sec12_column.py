# -*- coding: utf-8 -*-

def column(src_filename, col1_filename, col2_filename):
    """
    1列目をcol1.txtに，2列目をcol2.txtに保存
    """
    src_file = open(src_filename, 'r')
    col1_file = open(col1_filename, 'w')
    col2_file = open(col2_filename, 'w')

    col1_list, col2_list = [], []
    for line in src_file:
        cols = line.split('\t')
        col1_list.append(cols[0] + '\n')
        col2_list.append(cols[1] + '\n')

    col1_file.write(''.join(col1_list)), col2_file.write(''.join(col2_list))
    col1_file.close(), col2_file.close()
    return

def main():
    src_filename = '../src/hightemp.txt'
    col1_filename = './test/col1.txt'
    col2_filename = './test/col2.txt'
    column(src_filename, col1_filename, col2_filename)

if __name__ == '__main__':
    main()
