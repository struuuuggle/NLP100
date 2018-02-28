# -*- coding: utf-8 -*-
from sec30_load_mecab import load_mecab

def nouns():
    sentences = load_mecab('./test/neko.txt.mecab')
    noun_chains = set()
    for s in sentences:
        nouns = ''
        for m in s:
            if m['pos'] == '名詞':
                nouns += m['surface']
            else:
                if len(tmp) > 1:
                    noun_chains.add(nouns)
                nouns = ''

    # sort by the length of elements
    # ref. https://docs.python.jp/3/howto/sorting.html#key-functions
    sorted_noun_chains = sorted(noun_chains, key=lambda x: len(x))
    return sorted_noun_chains

def main():
    print(nouns())

if __name__ == '__main__':
    main()
