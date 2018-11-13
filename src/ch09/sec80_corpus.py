# -*- coding: utf-8 -*-
import bz2
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn


if __name__ == '__main__':
    # tokenize
    tokens = []
    with bz2.open('../../dat/enwiki-20150112-400-r10-105752.txt.bz2', 'r') as f:
        for line in f:
            words = line.decode().rstrip('\n').split(' ')

            # get rid of symbols from left and right side of token
            words = [word.strip(r'.,!?;:()[]\'"') for word in words]

            # for word in words:
            #     print(word)
            tokens += words

    # Remove empty items
    tokens.remove('')

    # output
    with open('./corpus.txt', 'w') as f:
        f.write(' '.join(tokens))
        f.write('\n')
