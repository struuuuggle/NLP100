# -*- coding: utf-8 -*-
import random

def typoglycemia(_str):
    _list = _str.split()
    for l in _list:
        if(len(l) >= 5):
            # 単語の先頭と末尾の文字を除いた部分文字列
            buf = l[1:-1]
            # シャッフル
            _list[_list.index(l)] = l[0] + ''.join(random.sample(buf, len(buf))) + l[-1]
    return ' '.join(_list)

def main():
    _str = input('>')
    print(typoglycemia(_str))

if __name__ == '__main__':
    main()
