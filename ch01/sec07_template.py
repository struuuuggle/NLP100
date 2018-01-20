# -*- coding: utf-8 -*-

def template(x, y, z):
    result = str(x) + "時の" + str(y) + "は" + str(z)
    print(result)

def main():
    template(12, "気温", 22.4)

if __name__ == '__main__':
    main()

