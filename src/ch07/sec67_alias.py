# -*- coding: utf-8 -*-
import pprint
import sys
from pymongo import MongoClient
client = MongoClient()
db = client.artist_database
collection = db.artist_collection

def search(alias_name):
    for doc in collection.find({'aliases.name' : alias_name}):
        pprint.pprint(doc)

def main():
    """
    入力したアーティストの別名をパラメータとして，クエリを検索

    # Examples
    $ python sec67_alias.py 'Dela Lachney'
    $ python sec67_alias.py 'Queen'
    """
    alias_name = sys.argv[1]
    search(alias_name)

if __name__ == '__main__':
    main()
