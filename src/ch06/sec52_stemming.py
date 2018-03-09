# -*- coding: utf-8 -*-
from sec51_words import words
from porter2stemmer import Porter2Stemmer

def stemming():
    stemmer = Porter2Stemmer()
    for w in words():
        print(w, stemmer.stem(w), sep='\t')


def main():
    stemming()

if __name__ == '__main__':
    main()
