# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pickle as pkl

def higher(array):
    x1 = array[0]
    x2 = array[1]
    if x1 >= x2:
        return x1
    return x2

if __name__ == '__main__':
    with open('model.bin', 'rb') as f1, open('feature.bin', 'rb') as f2:
        model = pkl.load(f1)
        feature = pkl.load(f2)

    with open('sentiment.bin', 'rb') as f:
        labels = pkl.load(f)

    # predict
    p_labels = model.predict(feature)
    probs = model.predict_proba(feature)

    for label,p_label,prob in zip(labels, p_labels, probs):
        print(f'{label}\t{p_label}\t{higher(prob)}')
