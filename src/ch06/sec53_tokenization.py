# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

"""
java -cp "/usr/local/lib/stanford-corenlp-full-2018-01-31/*" -mx3g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -outputFormat xml -file ../../lib/nlp.txt
"""

def tokenization():
    tree = ET.parse('./test/nlp.txt.xml')
    root = tree.getroot()
    for word in root.iter('word'):
        print(word.text)


def main():
    tokenization()

if __name__ == '__main__':
    main()
