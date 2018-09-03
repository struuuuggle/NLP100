# -*- coding: utf-8 -*-
import os
from random import shuffle


def data_configuration(pos, neg, ans):
    s_content = []

    with open(pos, 'r') as p:
        s_content += list(map(lambda line: '+1 ' + line, p.readlines()))

    with open(neg, 'r') as n:
        s_content += list(map(lambda line: '-1 ' + line, n.readlines()))

    shuffle(s_content)

    # generate sentiment.txt
    with open(ans, 'w') as s:
        s.writelines(s_content)


def count_valid_data():
    p_counter, n_counter = 0, 0
    with open(ans, 'r') as f:
        for line in f:
            if line[0:2] == '+1':
                p_counter += 1
            elif line[0:2] == '-1':
                n_counter += 1

    print('pos: {} neg: {}'.format(p_counter, n_counter))


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pos = os.path.normpath(os.path.join(current_dir, "../../lib/rt-polaritydata/rt-polarity.pos"))
    neg = os.path.normpath(os.path.join(current_dir, "../../lib/rt-polaritydata/rt-polarity.neg"))
    ans = os.path.normpath(os.path.join(current_dir, "./test/sentiment.txt"))

    data_configuration(pos, neg, ans)
    count_valid_data()
