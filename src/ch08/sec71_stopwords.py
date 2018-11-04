# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
import pickle
stopwords = set(stopwords.words('english') + [',', '.', '--', '(', ')', '"', ':', '!', '?', '+1', '-1'])

def check(word):
    return True if word in stopwords else False

def test():
    assert check('off')
    assert check('other')
    assert not check('take')
    assert not check('sightseeing')

    return True


if __name__ == '__main__':
    # test
    print(test())

    # save stopwords
    with open('./stopwords.bin', 'wb') as f:
        pickle.dump(stopwords, f)
