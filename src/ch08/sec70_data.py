# -*- coding: utf-8 -*-
import os
from random import shuffle
current_dir = os.path.dirname(os.path.abspath(__file__))
p_filename = os.path.join(current_dir, "../../lib/rt-polaritydata/rt-polaritydata/rt-polarity.pos")
n_filename = os.path.join(current_dir, "../../lib/rt-polaritydata/rt-polaritydata/rt-polarity.neg")
s_filename = os.path.join(current_dir, "./test/sentiment.txt")


def data_configuration():
    s_content = []

    with open(p_filename, 'r', encoding=ascii) as p:
        s_content += list(map(lambda line: '+1 ' + line, p.readlines()))

    with open(n_filename, 'r', encoding=ascii) as n:
        s_content += list(map(lambda line: '-1 ' + line, n.readlines()))

    shuffle(s_content)

    # generate sentiment.txt
    with open(s_filename, 'w') as s:
        s.writelines(s_content)


def count_valid_data():
    p_counter, n_counter = 0, 0
    with open(s_filename, 'r') as f:
        for line in f:
            if line[0:2] == '+1':
                p_counter += 1
            elif line[0:2] == '-1':
                n_counter += 1

    print('pos: {} neg: {}'.format(p_counter, n_counter))


if __name__ == '__main__':
    data_configuration()
    count_valid_data()
