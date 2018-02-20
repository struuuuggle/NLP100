# -*- coding: utf-8 -*-
import re

# 途中
def template(filename):
    # memo: 最短(非貪欲)マッチは/.*?/を使う
    template_regex = re.compile(r'''
    (?<=^\{\{基礎情報\s国\n)
    (.*)
    (?=^\}\}$)
    ''', re.MULTILINE | re.DOTALL | re.VERBOSE)

    fields_regex = re.compile(r'''
    (?<=^\|)
    (.+?)    # fields
    \s
    =
    \s
    (.+?)    # values
    (?=\n\|)
    ''', re.MULTILINE | re.DOTALL | re.VERBOSE)

    with open(filename, 'r') as f:
        contents = template_regex.search(f.read())
        tuples = fields_regex.findall(contents.group())
    dict = {}
    for tp in tuples:
        dict.setdefault(tp[0], tp[1])
    return dict


def main():
    print(template('./test/uk.txt'))

if __name__ == '__main__':
    main()
