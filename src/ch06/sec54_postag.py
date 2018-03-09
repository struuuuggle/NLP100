# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def postag():
    tree = ET.parse('./test/nlp.txt.xml')
    root = tree.getroot()
    for word, lemma, pos in zip(root.iter('word'), root.iter('lemma'), root.iter('POS')):
        print(word.text, lemma.text, pos.text, sep='\t')

def main():
    postag()

if __name__ == '__main__':
    main()
