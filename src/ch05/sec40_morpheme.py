# -*- coding: utf-8 -*-
import CaboCha

class Morph:
    """
    形態素を表すクラス
    """
    def __init__(self, _surface, _base, _pos, _pos1):
        self.surface = _surface
        self.base = _base
        self.pos = _pos
        self.pos1 = _pos1

    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.surface, self.base, self.pos, self.pos1)


def parse_txt(txt_filename, cabocha_filename):
    """
    txt_filenameの中身を係り受け解析してcabocha_filenameに出力する
    """
    with open(txt_filename, 'r') as source_file, open(cabocha_filename, 'w') as output_file:
        cabocha = CaboCha.Parser('-f1')
        for line in source_file:
            if line == '':
                continue
            output_file.write(cabocha.parseToString(line))

def load_morpheme(cabocha_filename):
    """
    cabocha_filenameから係り受け解析結果を読み込む(形態素)
    """
    with open(cabocha_filename, 'r') as f:
        docs = []
        sentence = []
        for line in f:
            # 空白とEOSは読み飛ばす
            if line[0] == '\u3000' or line == 'EOS':
                continue
            try:
                cols = line.split('\t')
                cols[1:] = cols[1].split(',')
            except IndexError:
                continue

            m = Morph(cols[0],    # 表層形
                      cols[7],    # 原形
                      cols[1],    # 品詞
                      cols[2],    # 品詞細分類1
            )
            sentence.append(m)

            if cols[0] == '。':
                docs.append(sentence)
                sentence  = []

    return docs


def main():
    #parse_txt('../../lib/neko.txt', './test/neko.txt.cabocha')
    print('surface\tbase\tpos\tpos1')
    for m in load_morpheme('./test/neko.txt.cabocha')[2]:
        print(m)


if __name__ == '__main__':
    main()
