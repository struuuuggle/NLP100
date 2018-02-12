# -*- coding: utf-8 -*-
import re

def categories(filename):
    category_regex = re.compile(r'\[\[Category:.*\]\]')
    with open(filename, 'r') as f:
        categories = category_regex.findall(f.read())
        result = '\n'.join(categories)
        print(result)
        return result


def main():
    categories('./test/uk.txt')

if __name__ == '__main__':
    main()
