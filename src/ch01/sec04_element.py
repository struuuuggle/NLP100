# -*- coding: utf-8 -*-

def element():
    dict = {}
    word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
    key = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    for i, w in enumerate(word):
        if (word.index(w) + 1) in key:
            dict[w[:1]] = i + 1
        else:
            dict[w[:2]] = i + 1

    return dict

if __name__ == '__main__':
    print(element())
