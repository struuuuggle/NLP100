# -*- coding: utf-8 -*-
import pickle as pkl
from sec72_features import extract_features
from sklearn.feature_extraction.text import CountVectorizer

if __name__ == '__main__':
    # load model
    with open('./model.bin', 'rb') as f:
        model = pkl.load(f)

    # load stopwords
    with open('./stopwords.bin', 'rb') as f:
        stopwords = pkl.load(f)

    # load vocab size
    with open('./vocab_size.bin', 'rb') as f:
        vocab = pkl.load(f)

    # extract features
    sentence = input('> ')
    buffer = extract_features(sentence)

    # transform features to vector
    vectorizer = CountVectorizer(vocabulary=vocab)
    feature_vec = vectorizer.fit_transform([buffer]).toarray()

    #predict
    label_predict = model.predict(feature_vec)
    prob = model.predict_proba(feature_vec)

    # print(f'label : {label_predict[0]}')
    print('label : {}'.format(label_predict[0]))
    # print(f'prob(+1): {round(prob[0][0] * 100, 3)}%')
    # print(f'prob(-1): {round(prob[0][1] * 100, 3)}%')
