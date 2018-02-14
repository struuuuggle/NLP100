# -*- coding: utf-8 -*-
import re

def mediafiles(filename):
    media_regex = re.compile(r'(?<=ファイル:).*\.\w+(?=\|\[\[.*\]\])')
    with open(filename, 'r') as f:
        result = media_regex.findall(f.read())
    for i, x in enumerate(result):
        result[i] = x.replace(' ', '_')
        print(result[i])
    return result

def main():
    mediafiles('./test/uk.txt')

if __name__ == '__main__':
    main()
