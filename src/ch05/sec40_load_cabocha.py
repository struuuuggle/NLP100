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
    def show(self):
        print(self.surface, self.base, self.pos, self.pos1, sep='\t')


def parse_txt(txt_filename, cabocha_filename):
    """
    txt_filenameの中身を係り受け解析してcabocha_filenameに出力する
    """
    with open(txt_filename, 'r') as source_file, open(cabocha_filename, 'w') as output_file:
        cabocha = CaboCha.Parser('-f1')
        output_file.write(cabocha.parseToString(source_file.read()))


def load_cabocha(cabocha_filename):
    """
    cabocha_filenameから係り受け解析結果を読み込む(形態素)
    """
    with open(cabocha_filename, 'r') as f:
        docs = []
        sentence = []
        for line in f:
            # 空白は読み飛ばす
            if line[0] == '\u3000':
                continue

            try:
                cols = line.split('\t')
                cols[1:] = cols[1].split(',')
            except IndexError:
                continue

            m = Morph(cols[0],    # 表層形
                      cols[6],    # 原形
                      cols[0],    # 品詞
                      cols[1],    # 品詞細分類1
            )
            sentence.append(m)

            if cols[0] == '。':
                docs.append(sentence)
                sentence  = []

    return docs


def main():
    #parse_txt('../../lib/neko.txt', './test/neko.txt.cabocha')
    for m in load_cabocha('./test/neko.txt.cabocha')[2]:
        m.show()


if __name__ == '__main__':
    main()
