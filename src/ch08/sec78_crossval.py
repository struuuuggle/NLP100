# -*- coding: utf-8 -*-
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn

from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
import pickle as pkl
import numpy as np

if __name__ == '__main__':
    with open('model.bin', 'rb') as f1, open('feature.bin', 'rb') as f2, open('sentiment.bin', 'rb') as f3:
        model = pkl.load(f1)
        feature = pkl.load(f2)
        label = pkl.load(f3)

    # preprocessing
    lb = preprocessing.LabelBinarizer()
    lb.fit(label)
    X = feature
    y = lb.transform(label).ravel()

    accuracy = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    precision = cross_val_score(model, X, y, cv=5, scoring='precision')
    recall = cross_val_score(model, X, y, cv=5, scoring='recall')
    f1 = cross_val_score(model, X, y, cv=5, scoring='f1')

    print(f'accuracy: {np.mean(accuracy)}')
    print(f'precision: {np.mean(precision)}')
    print(f'recall: {np.mean(recall)}')
    print(f'f1: {np.mean(f1)}')
