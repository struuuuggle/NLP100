# -*- coding: utf-8 -*-
from sec40_morpheme import Morph

class Chunk:
    """
    文節を表すクラス

    morphs:  形態素（Morphオブジェクト）のリスト
    dst:     係り先文節インデックス番号
    srcs:    係り元文節インデックス番号のリスト
    """
    def __init__(self):
        self.morphs = []
        self.dst = -100
        self.srcs = []
        self.surface = ''

    def __str__(self):
        return '{} \tfrom:{} \tto:{}'.format(self.surface, self.srcs, self.dst)


def load_chunk():
    with open('./test/neko.txt.cabocha', 'r') as f:
        sentences = []
        chunks = {}
        idx = -1
        for line in f:
            if line == 'EOS\n':
                l = sorted(chunks.items(), key=lambda x: x[0])
                sentences.append([tp[1] for tp in l])
                chunks.clear()

            # 文節の区切り情報を読み込む
            elif line[0] == '*':
                cols = line.split()
                idx = int(cols[1])
                dst = int(cols[2].rstrip('D'))

                if idx not in chunks:
                    chunks[idx] = Chunk()

                chunks[idx].dst = dst

                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            # 形態素解析結果を読み込む
            else:
                cols = line.split('\t')
                cols[1:] = cols[1].split(',')

                m = Morph(cols[0],    # 表層形
                          cols[7],    # 原形
                          cols[1],    # 品詞
                          cols[2],    # 品詞細分類1
                )
                chunks[idx].morphs.append(m)

    # chunk.surfaceを生成
    for chunks in sentences:
        for chunk in chunks:
            token = ''
            for m in chunk.morphs:
                if m.surface != '、' and m.surface != '。':
                    chunk.surface += m.surface

    return sentences



if __name__ == '__main__':
    sentences = load_chunk()
    sentence = sentences[7]
    for i, chunk in enumerate(sentence):
        print('{}: {}'.format(i, chunk))
