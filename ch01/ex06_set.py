# -*- coding: utf-8 -*-
from ex05_ngram import ngram

# 和集合
def union(X, Y):
    return X | Y

# 積集合
def intersection(X, Y):
    return X & Y

# 差集合 : Xの要素のうちYには含まれていない要素からなる集合
def difference(X, Y):
    return X - Y

# 対称差 : Aにのみ、Bにのみ含まれる要素からなる集合
def symmetricDifference(X, Y):
    return X ^ Y

def main():
    str1 = 'paraparaparadise'
    str2 = 'paragraph'
    target = 'se'
    
    X = set(ngram('char', 2, str1))
    Y = set(ngram('char', 2, str2))

    print('X =', X, sep='')
    print('Y =', Y, sep='')


    print('The union of X and Y:\n', union(X, Y), sep='')
    print('The intersection of X and Y:\n', intersection(X, Y), sep='')
    print('The difference of X and Y:\n', difference(X, Y) ,sep='')

    if target in X:
        print('\'', target, '\' is in X.', sep='')
    else:
        print('\'', target, '\' is not in X.', sep='')

    if target in Y:
        print('\'', target, '\' is in Y.', sep='')
    else:
        print('\'', target, '\' is not in Y.', sep='')

if __name__ == '__main__':
    main()
