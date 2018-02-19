# -*- coding: utf-8 -*-
import re
import json
import gzip

def extract_uk(filename):
    src_f =  gzip.open(filename, 'r')
    for line in src_f:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            with open('./test/uk.txt', 'w') as uk_f:
                uk_f.write(json_dict['text'])
            break
    src_f.close()

def main():
    extract_uk('../../lib/jawiki-country.json.gz')

if __name__ == '__main__':
    main()
