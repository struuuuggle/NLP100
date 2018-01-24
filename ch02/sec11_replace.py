# -*- coding: utf-8 -*-

def replace(inFile, outFile):
    outFile.write(inFile.read().replace('\t', ' '))

def main():
    inFile = open('../src/hightemp.txt', 'r')
    outFile = open('../src/sec11.txt', 'w')
    replace(inFile, outFile)

if __name__ == '__main__':
    main()
