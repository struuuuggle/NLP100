# -*- coding: utf-8 -*-
from sec30_load_mecab import load_mecab

def sahen_noun():
    sentences = load_mecab('./test/neko.txt.mecab')
    sahen_nouns = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos1'] == 'サ変接続':
                sahen_nouns.append(morpheme['surface'])
    return sahen_nouns

def main():
    print(sahen_noun())

if __name__ == '__main__':
    main()
