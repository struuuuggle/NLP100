# -*- coding: utf-8 -*-
import re

def category_name(filename):
    category_name_regex = re.compile(r'(?<=\[\[Category:).*(?=\]\])')
    with open(filename, 'r') as f:
        categories = category_name_regex.findall(f.read())
        result = '\n'.join(categories)
        print(result)
        return result


def main():
    category_name('./test/uk.txt')

if __name__ == '__main__':
    main()
