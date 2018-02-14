# -*- coding: utf-8 -*-
import re

def section(filename):
    section_regex = re.compile(r'^(?P<bracket>====|===|==)(?P<name>.*)(?P=bracket)$')
    with open(filename, 'r') as f:
        sections = []
        for line in f:
            m = section_regex.search(line)
            if m != None:
                sections.append((len(m.group('bracket')) - 1, m.group('name')))

    for x in sections:
        print('level:', x[0], ', name:', x[1])
    return sections


def main():
    section('./test/uk.txt')

if __name__ == '__main__':
    main()
