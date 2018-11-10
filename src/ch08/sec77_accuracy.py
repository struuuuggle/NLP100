# -*- coding: utf-8 -*-
import pickle as pkl
from sklearn.metrics import classification_report

if __name__ == '__main__':
    with open('model.bin', 'rb') as f1, open('feature.bin', 'rb') as f2:
        model = pkl.load(f1)
        feature = pkl.load(f2)

    with open('sentiment.bin', 'rb') as f:
        label = pkl.load(f)

    predict = model.predict(feature)

    target_names = ['+1', '-1']
    print(classification_report(label, predict, target_names=target_names))
