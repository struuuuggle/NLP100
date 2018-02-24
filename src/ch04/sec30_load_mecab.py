# -*- coding: utf-8 -*-
import MeCab

neko_txt = '../../lib/neko.txt'
neko_txt_mecab = './test/neko.txt.mecab'

def parse_txt(txt, txt_mecab):
    with open(txt, 'r') as in_f, open(txt_mecab, 'w') as out_f:
        mecab = MeCab.Tagger()
        out_f.write(mecab.parse(in_f.read()))

def load_mecab(txt_mecab):
    # neko.txtを形態素解析してneko.txt.mecabに保存する
    with open(txt_mecab, 'r') as f:
        docs = []
        sentence = []
        for line in f:
            try:
                cols = line.split('\t')
                details = cols[1].split(',')
            except IndexError:
                continue

            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            morpheme = {'surface' : cols[0],      # 表層形
                        'base'    : details[6],   # 原形
                        'pos'     : details[0],   # 品詞
                        'pos1'    : details[1],   # 品詞細分類1
            }
            sentence.append(morpheme)

            if cols[0] == '。':
                docs.append(sentence)
                sentence  = []

        return docs

def main():
    parse_txt(neko_txt, neko_txt_mecab)
    print(load_mecab(neko_txt_mecab))

if __name__ == '__main__':
    main()
