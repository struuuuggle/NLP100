# -*- coding: utf-8 -*-
import re
from sec25_template import template

def remove_markup():
    markup_regex = re.compile(r'\'{2,5}')
    dict = template('./test/uk.txt')
    # ここ、もっとスタイリッシュに書けそう
    #for k, v in zip(dict.keys(), dict.values()):
    for k, v in dict.items():
        dict[k] = markup_regex.sub('', v)
    return dict

def main():
    print(remove_markup())

if __name__ == '__main__':
    main()
