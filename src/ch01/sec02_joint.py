# -*- coding: utf-8 -*-

def joint():
    for (a, b) in zip("パトカー", "タクシー"):
        print(a + b, end='')

def main():
    joint()
    
if __name__ == '__main__':
    main()
