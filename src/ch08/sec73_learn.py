# -*- coding: utf-8 -*-
from sklearn.linear_model import LogisticRegression
import pickle as pkl

if __name__ == '__main__':
    with open('./feature.bin', 'rb') as f, open('./sentiment.bin', 'rb') as s:
        x = pkl.load(f)
        y = pkl.load(s)

    # learn
    model = LogisticRegression(random_state = 0).fit(x, y)

    # save
    with open('./model.bin', 'wb') as f:
        pkl.dump(model, f)
