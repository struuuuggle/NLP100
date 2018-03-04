# -*- coding: utf-8 -*-
import re

def split(filename):
    pattern = re.compile(r'(?<=[\.\;\:\?\!])\s+(?=[A-Z])|\n{2}(?=[A-Z])', re.DOTALL | re.MULTILINE)
    with open(filename, 'r') as f:
        return [s.rstrip() for s in re.split(pattern, f.read())]

def main():
    for sentence in split('../../lib/nlp.txt'):
        print(sentence)

if __name__ == '__main__':
    main()
