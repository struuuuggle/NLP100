# -*- coding: utf-8 -*-
import os
import json
import gzip
import pymongo
from pymongo import MongoClient
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/artist.json.gz")
client = MongoClient()
db = client.artist_database
collection = db.artist_collection

def build(filename):
    with gzip.open(filename, 'r') as f:
        print("=== Inserting ===")
        posts = []
        for i, line in enumerate(f):
            j = json.loads(line)
            posts.append(j)

            if i % 50000 == 0:
                collection.insert_many(posts)
                posts.clear()
                print('Inserted {} queries...'.format(i))

        if len(posts) > 0:
            collection.insert_many(posts)
            print('Inserted {} queries...'.format(i))

        print("Done.")

        print("=== Indexing ===")
        collection.create_index([('name', pymongo.ASCENDING)])
        collection.create_index([('aliases.name', pymongo.ASCENDING)])
        collection.create_index([('tags.value', pymongo.ASCENDING)])
        collection.create_index([('rating.value', pymongo.ASCENDING)])
        print("Done.")


def main():
    # Take a while
    build(data)

if __name__ == '__main__':
    main()
