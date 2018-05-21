# -*- coding: utf-8 -*-
import CaboCha
from graphviz import Digraph
from sec40_morpheme import Morph
from sec41_chunk import Chunk

def get_chunk(sentence):
    tree = cabocha.parse(sentence)
    res = tree.toString(CaboCha.FORMAT_LATTICE).split('\n')
    res.remove('')

    sentence = list()
    chunks = dict()
    idx = -1
    for line in res:
        if line == 'EOS':
            l = sorted(chunks.items(), key=lambda x: x[0])
            sentence = [tp[1] for tp in l]
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
    for chunk in sentence:
        token = ''
        for m in chunk.morphs:
            if m.surface != '、' and m.surface != '。':
                chunk.surface += m.surface

    return sentence


def visualize(idx, chunks):
    G = Digraph(format='png')
    G.attr('node', share='chircle')

    # グラフを作成
    for i, chunk in enumerate(chunks):
        G.node(str(i), chunk.surface)

    for i, chunk in enumerate(chunks):
        if chunk.dst != -1:
            G.edge(str(i), str(chunk.dst))

    G.render('./test/sec44-' + str(idx))


if __name__ == '__main__':
    cabocha = CaboCha.Parser('--charset=UTF8')
    sentences = [
        '太郎はこの本を次朗を見た女性に渡した．',
        '30年も前に言語と画像を研究していた．',
    ]
    for i, s in enumerate(sentences):
        chunks = get_chunk(s)
        visualize(i, chunks)
