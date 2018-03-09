# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def persons():
    tree = ET.parse('./test/nlp.txt.xml')
    root = tree.getroot()

    persons = []
    for token in root.iter('token'):
        if token.find('NER').text == 'PERSON':
            persons.append(token.find('word').text)
    return persons

def main():
    for p in persons():
        print(p)

if __name__ == '__main__':
    main()
