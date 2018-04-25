# -*- coding: utf-8 -*-
import json
from pymongo import MongoClient
client = MongoClient()
db = client.artist_database
collection = db.artist_collection

def query(area_name):
    """
    $ db.artist_collection.count( { 'area': 'Japan' } );
    """
    return collection.count({'area' : area_name})

def main():
    print(query('Japan'))

if __name__ == '__main__':
    main()
