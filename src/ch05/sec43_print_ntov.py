# -*- coding: utf-8 -*-
from sec41_chunk import load_chunk

def find_pos(posname, chunk):
    for m in chunk.morphs:
        if m.pos == posname:
            return True
    return False


def print_ntov():
    sentences = load_chunk()
    for i, chunks in enumerate(sentences):
        for chunk in chunks:
            if find_pos('名詞', chunk) and find_pos('動詞', chunks[chunk.dst]) and chunk.dst != -1:
                print('{}\t{}'.format(chunk.surface, chunks[chunk.dst].surface))


if __name__ == '__main__':
    print_ntov()
