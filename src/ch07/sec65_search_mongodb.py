# -*- coding: utf-8 -*-
import pprint
from pymongo import MongoClient
client = MongoClient()
db = client.artist_database
collection = db.artist_collection

def search_mongodb(artist_name):
    for doc in collection.find({'name' : artist_name}):
        pprint.pprint(doc)

def main():
    search_mongodb('Queen')

if __name__ == '__main__':
    main()
