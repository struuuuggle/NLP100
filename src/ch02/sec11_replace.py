# -*- coding: utf-8 -*-
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/hightemp.txt")
output = os.path.join(current_dir, "./test/tab2space.txt")

def tab2space(data):
    with open(data, 'r') as tabf, open(output, 'w') as spacef:
        spacef.write(tabf.read().replace('\t', ' '))

def main():
    tab2space(data)
    # 以下のコマンドで確認
    # cat ../src/hightemp.txt | tr "\t" " "

if __name__ == '__main__':
    main()
