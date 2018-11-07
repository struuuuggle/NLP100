# -*- coding: utf-8 -*-
import os

# 以下のコマンドで確認
# cat hightemp.txt | tr "\t" " "

DIR = os.path.dirname(os.path.abspath(__file__))
IN_PATH  = os.path.join(DIR, "../../dat/hightemp.txt")
OUT_PATH = os.path.join(DIR, "./test/sec11_tab2space.txt")


def tab2space(path1=IN_PATH, path2=OUT_PATH):
    with open(path1, 'r') as f1, open(path2, 'w') as f2:
        f2.write(f1.read().replace('\t', ' '))


if __name__ == '__main__':
    tab2space()
