# -*- coding: utf-8 -*-
from sec30_load_mecab import load_mecab

def a_of_b():
    sentences = load_mecab('./test/neko.txt.mecab')
    res = []
    for sentence in sentences:
        for i in range(len(sentence)):
            try:
                w1 = sentence[i]
                w2 = sentence[i + 1]
                w3 = sentence[i + 2]
            except IndexError:
                continue
            if w1['pos'] == '名詞' and w2['surface'] == 'の' and w3['pos'] == '名詞':
                res.append(w1['surface'] + w2['surface'] + w3['surface'])
    return res


def main():
    print(a_of_b())

if __name__ == '__main__':
    main()
