# -*- coding: utf-8 -*-
import sys
import numpy as np
import pickle as pkl
from nltk import FreqDist
from nltk import stem
from sec71_stopwords import check, stopwords
from sklearn.feature_extraction.text import CountVectorizer

TXT_PATH = './test/sentiment.txt'

# 素性抽出器
def extract_features(sentence):
    words = sentence.split()
    stemmer = stem.PorterStemmer()
    result = [stemmer.stem(word) for word in words if not check(word)]
    return ' '.join(result)


if __name__ == '__main__':
    with open('stopwords.bin', 'rb') as f:
        stopwords = pkl.load(f)

    corpus = []
    labels = []
    for line in open(TXT_PATH, 'r'):
        corpus.append(extract_features(line.strip()[3:]))
        labels.append(line[:2])

    # print(corpus)
    vectorizer = CountVectorizer()
    feature = vectorizer.fit_transform(corpus).toarray()
    sentiment = np.array(labels)

    # save feature and sentiment
    with open('feature.bin', 'wb') as f, open('sentiment.bin', 'wb') as s:
        pkl.dump(feature, f)
        pkl.dump(sentiment, s)

    # save the size of vocab
    with open('vocab_size.bin', 'wb') as f1, open('vocab.bin', 'wb') as f2:
        pkl.dump(vectorizer.vocabulary_, f1)
        pkl.dump(vectorizer.get_feature_names(), f2)
