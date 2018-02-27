# -*- coding: utf-8 -*-
from sec36_freq import freq
from collections import Counter
import Gnuplot

def histogram():
    sorted_words = freq()

    filename = './test/38_histogram.dat'
    with open(filename, 'w') as f:
        for tp in sorted_words:
            f.write(str(tp[1]) + ' ' + str(tp[0]) + '\n')

    # Gnuplotでグラフを描画
    gp = Gnuplot.Gnuplot()
    gp('set term aqua font "ヒラギノ丸ゴ ProN W4, 10"')
    gp('set style fill solid')
    gp.set(xlabel="出現頻度",
           ylabel="単語の種類数",
           xrange=(0.5, 20),
           title="[NLP100-38] ヒストグラム")
    gp('filter(x,y)=int(x/y)*y')
    # filterの第二引数でいくつごとにまとめるかを選ぶ
    gp.plot('"' + filename + '" using (filter($1,1)):(1) smooth frequency with boxes notitle')

def alter_histogram():
    sorted_words = freq()
    c = Counter([tp[1] for tp in sorted_words]).most_common()

    filename = './test/38_histogram.dat'
    with open(filename, 'w') as f:
        for tp in c:
            f.write(str(tp[0]) + ' ' + str(tp[1]) + '\n')

    # Gnuplotでグラフを描画
    gp = Gnuplot.Gnuplot()
    gp('set term aqua font "ヒラギノ丸ゴ ProN W4, 10"')
    gp('set style fill solid')
    gp.set(xlabel="出現頻度",
           ylabel="単語の種類数",
           xrange=(-0.5, 20),
           title="[NLP100-38] ヒストグラム")
    gp('plot "' + filename  + '" using 0:2 with boxes notitle')

def main():
    #histogram()
    alter_histogram()

if __name__ == '__main__':
    main()
