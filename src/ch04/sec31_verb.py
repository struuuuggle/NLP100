# -*- coding: utf-8 -*-
from sec30_load_mecab import load_mecab

def extract_verb():
    sentences = load_mecab('./test/neko.txt.mecab')
    verbs = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == '動詞':
                verbs.append(morpheme['surface'])
    return verbs

def main():
    print(extract_verb())

if __name__ == '__main__':
    main()
