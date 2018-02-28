# -*- coding: utf-8 -*-
import re
from sec26_markup import remove_markup

def innerlink():
    innerlink_regex = re.compile(r'\[\[(?:.*?\|)*(.+?)\]\]')
    dict = remove_markup()
    #for k, v in zip(dict.keys(), dict.values()):
    for k, v in dict.items():
        dict[k] = innerlink_regex.sub(r'\1', v)
    return dict

def main():
    print(innerlink())

if __name__ == '__main__':
    main()
