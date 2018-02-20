# -*- coding: utf-8 -*-
import re
from sec27_innerlink import innerlink

def mediawiki():
    link_website_regex = re.compile(r'\[.*?\s(.*?)\]', re.DOTALL)
    template_regex = re.compile(r'\{\{(?:.*?\|)*(.+?)\}\}')
    tag_regex = re.compile(r'\<\/?ref\>|\<br\/\>')
    reference_regex = re.compile(r'\<ref\sname\=\".*?\"(\s\/)?\>')

    dict = innerlink()

    # 外部リンクを除去
    for k, v in zip(dict.keys(), dict.values()):
        dict[k] = link_website_regex.sub(r'(\1)', v)

    # テンプレートを除去
    for k, v in zip(dict.keys(), dict.values()):
        dict[k] = template_regex.sub(r'\1', v)

    # タグ(<ref>, </ref>, <br/>)を除去
    for k, v in zip(dict.keys(), dict.values()):
        dict[k] = tag_regex.sub('', v)

    # <ref name="NAME">を除去
    for k, v in zip(dict.keys(), dict.values()):
        dict[k] = reference_regex.sub('', v)

    return dict

def main():
    print(mediawiki())

if __name__ == '__main__':
    main()