# -*- coding: utf-8 -*-
from sec36_freq import freq
import Gnuplot

def zipf():
    sorted_words = freq()

    # 1列目に出現頻度順位、2列目に出現頻度
    filename = './test/39_zipf.dat'
    with open(filename, 'w') as f:
        for i, tp in enumerate(sorted_words):
            f.write(str(i + 1) + ' ' + str(tp[1]) + '\n')

    # Gnuplotで両対数グラフを描画
    gp = Gnuplot.Gnuplot()
    gp('set term aqua font "ヒラギノ丸ゴ ProN W4, 10"')
    gp.set(xlabel="log(rank)",
           ylabel="log(frequency)",
           title="[NLP100-39] Zipfの法則")
    gp('set logscale x')
    gp('set logscale y')
    gp.plot('"' + filename + '" with points ps 1')



def main():
    zipf()

if __name__ == '__main__':
    main()
