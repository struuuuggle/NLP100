# -*- coding: utf-8 -*-

def pi():
    word = []
    char_len = []
    word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".split()
    
    for w in word:
        char_len.append(len(w))

    print(char_len)

def main():
    pi()

if __name__ == '__main__':
    main()
