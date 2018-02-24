# -*- coding: utf-8 -*-
from sec30_load_mecab import load_mecab

def base_of_verb():
    sentences = load_mecab('./test/neko.txt.mecab')
    base_of_verbs = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == '動詞':
                base_of_verbs.append(morpheme['base'])
    return base_of_verbs

def main():
    print(base_of_verb())

if __name__ == '__main__':
    main()
