# -*- coding: utf-8 -*-
import random

def typoglycemia(_str):
    l = _str.split()
    for s in l:
        if(len(s) >= 5):
            # 単語の先頭と末尾の文字を除いた部分文字列
            buf = s[1:-1]
            # シャッフル
            l[l.index(s)] = s[0] + ''.join(random.sample(buf, len(buf))) + s[-1]
    return ' '.join(l)


if __name__ == '__main__':
    print('Type a sentence ...')
    buffer = input('>')
    print(typoglycemia(buffer))
