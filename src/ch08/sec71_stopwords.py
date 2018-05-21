# -*- coding: utf-8 -*-
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english') + [',', '.', '--', '(', ')', '"', ':', '!', '?', '+1', '-1'])

def judge(word):
    if word in stopwords:
        return True
    else:
        return False


def test_judge():
    if not judge('off'):
        print('\'off\' must be in stopwords but not found')
        return False
    if not judge('other'):
        print('\'other\' must be in stopwords but not found')
        return False

    if judge('take'):
        print('\'take\' must not be in stopwords but found')
        return False
    if judge('sightseeing'):
        print('\'sightseeing\' must not be in stopwords but found')
        return False

    return True


if __name__ == '__main__':
    print(test_judge())
