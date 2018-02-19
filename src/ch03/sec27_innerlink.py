# -*- coding: utf-8 -*-
import re
from sec26_markup import remove_markup

def innerlink():
    # [[記事名|表示文字]]の形式の時には記事名は取り出される
    # できれば表示文字を取り出したい
    innerlink_regex = re.compile(r'\[\[(.+?)(\|.+)?\]\]')
    dict = remove_markup()
    for k, v in zip(dict.keys(), dict.values()):
        dict[k] = innerlink_regex.sub(r'\1', v)
    return dict

def main():
    print(innerlink())

if __name__ == '__main__':
    main()
