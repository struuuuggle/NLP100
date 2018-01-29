# -*- coding: utf-8 -*-

def element():
    element = []
    word = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
    key = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    for w in word:
        if (word.index(w) + 1) in key:
            # 単語の先頭の1文字をelementに追加
            element.append(w[:1])
        else:
            # 単語の先頭の2文字をelementに追加
            element.append(w[:2])

    print(element)

def main():
    element()

if __name__ == '__main__':
    main()
