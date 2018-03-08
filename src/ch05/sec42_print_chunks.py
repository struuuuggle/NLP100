# -*- coding: utf-8 -*-
from sec41_chunk import load_chunk

def print_chunks():
    sentences = load_chunk()
    for chunks in sentences:
        for chunk in chunks:
            if chunk.dst != -1:
                dst_surface = chunks[chunk.dst].surface
            else:
                dst_surface = 'EOS'
            print('{}\t{}'.format(chunk.surface, dst_surface))

def main():
    print_chunks()

if __name__ == '__main__':
    main()
