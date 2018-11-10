# -*- coding: utf-8 -*-
import warnings
def warn(*args, **kwargs):
    pass
warnings.warn = warn

import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn import preprocessing
import pickle as pkl

if __name__ == '__main__':
    with open('model.bin', 'rb') as f1, open('feature.bin', 'rb') as f2, open('sentiment.bin', 'rb') as f3:
        model = pkl.load(f1)
        feature = pkl.load(f2)
        label = pkl.load(f3)

    # preprocessing
    lb = preprocessing.LabelBinarizer()
    lb.fit(label)

    X = feature
    y_true = lb.transform(label).ravel()
    y_score = model.predict_proba(X)[:, 1]

    precision, recall, threshold = precision_recall_curve(y_true, y_score)

    plt.plot(recall, precision)
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title('Precision-Recall curve')
    plt.show()
