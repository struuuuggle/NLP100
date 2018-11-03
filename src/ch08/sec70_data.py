# -*- coding: utf-8 -*-

"""
Usage: python sec70_data.py <PATH_TO_POS_FILE> <PATH_TO_NEG_FILE>
"""
import sys
from random import shuffle

POS_PATH = sys.argv[1]
NEG_PATH = sys.argv[2]
ANS_PATH = sys.argv[3]

def data_configuration(pos = POS_PATH, neg = NEG_PATH, ans = ANS_PATH):
    s_content = []

    with open(pos, 'r') as p:
        s_content += list(map(lambda line: '+1 ' + line, p.readlines()))

    with open(neg, 'r') as n:
        s_content += list(map(lambda line: '-1 ' + line, n.readlines()))

    shuffle(s_content)

    # generate sentiment.txt
    with open(ans, 'w') as s:
        s.writelines(s_content)


def count_valid_data(ans = ANS_PATH):
    p_counter, n_counter = 0, 0
    with open(ans, 'r') as f:
        for line in f:
            if line[0:2] == '+1':
                p_counter += 1
            elif line[0:2] == '-1':
                n_counter += 1

    print('pos: {} neg: {}'.format(p_counter, n_counter))


if __name__ == '__main__':
    data_configuration()
    count_valid_data()
