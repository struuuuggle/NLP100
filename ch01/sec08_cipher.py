# -*- coding: utf-8 -*-

import sys

def cipher(_str):
    code = ''
    for w in _str:
        if w.islower():
            code += chr(219 - ord(w))
        else:
            code += w
    return code


def decipher(code):
    decode = ''
    for w in code:
        if w.islower():
            decode += chr(219 - ord(w))
        else:
            decode += w
    return decode


def main():
    plaintext = sys.argv[1]
    code = cipher(plaintext)
    decode = decipher(code)
    print('code :', code)
    print('deode:', decode)

if __name__ == '__main__':
    main()
