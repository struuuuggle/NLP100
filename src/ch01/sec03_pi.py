# -*- coding: utf-8 -*-

def pi_list():
    l = []
    word = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".split()

    for w in word:
        l.append(len(w.rstrip(',')))

    return l

if __name__ == '__main__':
    print(pi_list())
