# -*- coding: utf-8 -*-
import re

# 途中
def template(filename):
    # memo: 最短(非貪欲)マッチは/.*?/を使う
    template_regex = re.compile(r'\{\{.*?\}\}')
    with open(filename, 'r') as f:
        result = template_regex.findall(f.read())
    for x in result:
        print(x)


def main():
    template('./test/uk.txt')

if __name__ == '__main__':
    main()
