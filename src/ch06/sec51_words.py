# -*- coding: utf-8 -*-
import re
from sec50_split import split

def words():
    # e.g.がe.gになる
    # -- が一単語として数えられてしまっている
    sentences = split('../../lib/nlp.txt')
    for s in sentences:
        for w in re.split(r'\s', s):
            yield w.strip(',.;:?!()"')
        yield ''

def main():
    for w in words():
        print(w)

if __name__ == '__main__':
    main()
