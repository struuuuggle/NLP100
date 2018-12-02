# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('./sec80_corpus.txt', 'r') as corpus, open('./country.txt', 'r') as countries:
        corpus_str = corpus.read()
        for country in countries:
            corpus_str = corpus_str.replace(country.rstrip(), country.rstrip().replace(' ', '_'))

    with open('./sec81_corpus.txt', 'w') as f:
        print(corpus_str, file=f)
