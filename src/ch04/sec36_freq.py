# -*- coding: utf-8 -*-
from sec30_load_mecab import load_mecab
from collections import Counter

def freq():
    sentences = load_mecab('./test/neko.txt.mecab')
    words = [morpheme['surface'] for sentence in sentences for morpheme in sentence]
    sorted_words = [tp for tp in Counter(words).most_common()]
    return sorted_words

def main():
    print(freq())

if __name__ == '__main__':
    main()
