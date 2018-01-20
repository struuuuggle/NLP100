# -*- coding: utf-8 -*-

def element():
    element = []
    word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
    key = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    for w in word:
        if (word.index(w) + 1) in key:
            element.append(w[:1])
        else:
            element.append(w[:2])

    print(element)

def main():
    element()

if __name__ == '__main__':
    main()
