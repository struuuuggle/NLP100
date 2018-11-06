# -*- coding: utf-8 -*-

def template(x, y, z):
    result = str(x) + "時の" + str(y) + "は" + str(z)
    print(result)

if __name__ == '__main__':
    template(12, "気温", 22.4)
