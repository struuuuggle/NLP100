# -*- coding: utf-8 -*-
from sec30_load_mecab import load_mecab
from collections import Counter
import Gnuplot

def freq_top10():
    sentences = load_mecab('./test/neko.txt.mecab')
    words = [morpheme['surface'] for sentence in sentences for morpheme in sentence]
    top10_words = [tp for tp in Counter(words).most_common(10)]

    # 頻度上位10語とその出現頻度をdatファイルに書き出す
    with open('./test/top10.dat', 'w') as f:
        for x in top10_words:
            f.write(x[0] + ' ' + str(x[1]) + '\n')

    # Gnuplotでグラフを描画
    gp = Gnuplot.Gnuplot()
    gp('set term aqua font "ヒラギノ丸ゴ ProN W4, 16"')
    gp('set boxwidth 0.5 relative')
    gp('set style fill solid border lc rgb "black"')
    gp.xlabel("word")
    gp.ylabel("frequency")
    gp.plot('"./test/top10.dat" using 0:2:xtic(1) with boxes lw 2 notitle')


def main():
    freq_top10()

if __name__ == '__main__':
    main()
