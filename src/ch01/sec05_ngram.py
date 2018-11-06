# -*- coding: utf-8 -*-

def word_ngram(num , seq):
    # シーケンスの種類で場合分け
    if seq.__class__ == 'str':
        words = seq
    else:
        words = seq.split()

    return [words[i] + words[i+1] for i in range(0, len(words) - 1)]


def char_ngram(num, seq):
    # シーケンスの種類で場合分け
    if seq.__class__ == 'list':
        chars = ''.join(seq)
    else:
        chars = seq

    return [chars[i:i+2] for i in range(0, len(chars))]


if __name__ == '__main__':
    s = "I am an NLPer"
    #string = ['I', 'am', 'an', 'NLPer']
    print("単語bi-gram: ")
    print(word_ngram(2, s))
    print("文字bi-gram: ")
    print(char_ngram(2, s))
