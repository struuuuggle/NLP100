# -*- coding: utf-8 -*-
import re
import json

def extract_uk(filename):
    src_f =  open(filename, 'r')
    for line in src_f:
        # Do not use 'json.loads()'
        json_dict = json.load(line)
        if json_dict['title'] == 'イギリス':
            with open('./test/uk.txt', 'w') as uk_f:
                uk_f.write(json_dict['text'])
            break
    src_f.close()

def main():
    extract_uk('../src/jawiki-country.json')

if __name__ == '__main__':
    main()
