# -*- coding: utf-8 -*-
from collections import defaultdict
from tqdm import tqdm
from sklearn.externals import joblib
from scipy.sparse import lil_matrix


if __name == '__main__':
    N = 0
    vocab = joblib.load('vocab.joblib')
    matrix = lil_matrix(len(vocab), len(vocab))

    for pair in tqdm(open('sec82_context.txt')):
        word, c_word = pair.rstrip().split('\t')
        idx_t = vocab[word]
        idx_c = vocab[c_word]
        matrix[idx_t, idx_c] += 1
        N += 1

    print(f'N = {N}')
    joblib.dump(matrix, 'matrix.joblib')
