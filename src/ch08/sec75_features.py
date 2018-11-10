# -*- coding: utf-8 -*-
import pickle as pkl

if __name__ == '__main__':
    # load model, vocab
    with open('model.bin', 'rb') as f1, open('vocab.bin', 'rb') as f2:
        model = pkl.load(f1)
        vocab = pkl.load(f2)

    weight = [(i, w) for i, w in enumerate(model.coef_.tolist()[0])]
    weight2 = sorted(weight, key=lambda x: x[1])

    print('=== Highest 10 ===')
    for i, tp in enumerate(weight2[:10]):
        print(f'{i+1}: {vocab[tp[0]]}')

    print('=== Lowest 10 === ')
    for i, tp in enumerate(weight2[:-11:-1]):
        print(f'{i+1}: {vocab[tp[0]]}')
