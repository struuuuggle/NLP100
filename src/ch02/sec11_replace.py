# -*- coding: utf-8 -*-

def replace(filename1, filename2):
    inFile = open(filename1, 'r')
    outFile = open(filename2, 'w')
    outFile.write(inFile.read().replace('\t', ' '))

def main():
    filename1 = '../../lib/hightemp.txt'
    filename2 = './test/sec11.txt'
    replace(filename1, filename2)
    # 以下のコマンドで確認
    # cat ../src/hightemp.txt | tr "\t" " "

if __name__ == '__main__':
    main()
