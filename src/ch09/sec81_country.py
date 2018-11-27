# -*- coding: utf-8 -*-

if __name__ == '__main__':
    countries = set([line.rstrip('\n') for line in open('./country.txt', 'r')])

    with open('./sec81_corpus.txt', 'w') as f:
        for line in open('./sec80_corpus.txt', 'r'):
            words = set(line.rstrip()split(' '))
            if countries & words:
                for country in open('./country.txt', 'r'):
                    country = country.rstrip()
                    line = line.replace(country, country.replace(' ', '_'))
            f.write(line)
