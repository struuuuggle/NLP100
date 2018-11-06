# -*- coding: utf-8 -*-
from sec05_ngram import word_ngram, char_ngram

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


if __name__ == '__main__':
    s1 = 'paraparaparadise'
    s2 = 'paragraph'
    target = 'se'

    X = set(char_ngram(2, s1))
    Y = set(char_ngram(2, s2))

    print(f'X = {X}')
    print(f'Y = {Y}')

    print('The union of X and Y:\n', union(X, Y), sep='')
    print('The intersection of X and Y:\n', intersection(X, Y), sep='')
    print('The difference of X and Y:\n', difference(X, Y), sep='')

    if target in X:
        print(f'\'{target}\' is in X.')
    else:
        print(f'\'{target}\' is not in X.')

    if target in Y:
        print(f'\'{target}\' is in Y.')
    else:
        print(f'\'{target}\' is not in Y.')
