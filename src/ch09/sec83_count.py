# -*- coding: utf-8 -*-
# from tqdm import tqdm
# from sklearn.externals import joblib
# from scipy.sparse import lil_matrix

from tqdm import tqdm
from collections import Counter
import pickle

if __name__ == '__main__':
    # vocab = joblib.load('vocab.joblib')
    # matrix = lil_matrix((len(vocab), len(vocab)))

    # N = 0
    # for pair in tqdm(open('sec82_context.txt')):
    #     word, c_word = pair.rstrip().split('\t')
    #     idx_t = vocab[word]
    #     idx_c = vocab[c_word]
    #     matrix[idx_t, idx_c] += 1
    #     N += 1

    # print(f'N = {N}')
    # joblib.dump(matrix, 'matrix.joblib')

    f_tc, f_tx, f_xc = Counter(), Counter(), Counter()
    N = 0

    for line in tqdm(open('./sec82_context.txt')):
        try:
            t, c = line.strip().split('\t')
        except ValueError:
            continue
        f_tc[t, c] += 1
        f_tx[t] += 1
        f_xc[c] += 1
        N += 1

    with open('./sec83_count.bin', 'wb') as f:
        pickle.dump([f_tc, f_tx, f_xc, N], f)

    print(f'f(t,c) = {f_tc}')
    print(f'f(t,*) = {f_tx}')
    print(f'f(*,c) = {f_xc}')
    print(f'N = {N}')
