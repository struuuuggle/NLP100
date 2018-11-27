# -*- coding: utf-8 -*-
from random import randint
from collections import defaultdict
from sklearn.externals import joblib

CORPUS_PATH = "./sec81_corpus.txt"
OUTPUT_PATH = "./sec82_context.txt"

if __name__ == '__main__':
    vocab = defaultdict(lambda: len(vocab))
    with open(CORPUS_PATH) as f:
        words = f.read().rstrip().split(' ')

    with open(OUTPUT_PATH, 'w') as f:
        for i, t in enumerate(words):
            vocab[t]
            d = randint(1, 5)
            for j in range(1, d + 1):
                if i+j < len(words):
                    f.write(f'{t}\t{words[i+j]}\n')
                if i-j >= 0:
                    f.write(f'{t}\t{words[i-j]}\n')

    joblib.dump(dict(vocab), 'vocab.joblib')
