# -*- coding: utf-8 -*-
import re
import json

def extract_uk(filename):
    src_f =  open(filename, 'r')
    for line in src_f:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            with open('./test/uk.txt', 'w') as uk_f:
                uk_f.write(json_dict['text'])
            break
    src_f.close()

def main():
    extract_uk('../../lib/jawiki-country.json')

if __name__ == '__main__':
    main()
