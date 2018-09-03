# -*- coding: utf-8 -*-
import sys
import os
import nltk
from porter2stemmer import Porter2Stemmer
from sec71_stopwords import stopwords

# 素性抽出器
def review_features(review, word_features):
    review_words = set(review)
    features = {}
    for word in word_features:
        features['contain({})'.format(word)] = (word in review_words)
    return features



    # stem
    #stemmer = Porter2Stemmer()
    #return [stemmer.stem(t) for t in p+n]



if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pos = os.path.normpath(os.path.join(current_dir, "../../lib/rt-polaritydata/rt-polarity.pos"))
    neg = os.path.normpath(os.path.join(current_dir, "../../lib/rt-polaritydata/rt-polarity.neg"))

    with open(pos, 'r') as p, open(neg, 'r') as n:
        content = p.read() + n.read()
        all_words = nltk.FreqDist(w for w in content)
    print(all_words.keys())
    word_features = list(all_words)[:500]
