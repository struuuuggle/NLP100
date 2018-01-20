# -*- coding: utf-8 -*-

def ngram(option, num, seq):

    # 単語n-gramの生成
    if option == 'word':

        # シーケンスの種類で場合分け
        if seq.__class__ == 'str':
            _words = seq
        else:
            _words = seq.split()
        
        result = [_words[i] + _words[i+1] for i in range(0, len(_words) - 1)]
        print(result)
        return

    # 文字n-gramの生成
    elif option == 'char':

        # シーケンスの種類で場合分け
        if seq.__class__ == 'list':
            _str = ''.join(seq)
        else:
            _str = seq
        
        result = [_str[i:i+2] for i in range(0, len(_str))]
        print(result)
        return

def main():
    string = "I am an NLPer"
    #string = ['I', 'am', 'an', 'NLPer']
    print("単語bi-gram: ")
    ngram("word", 2, string)
    print("文字bi-gram: ")
    ngram("char", 2, string)

if __name__ == '__main__':
    main()

