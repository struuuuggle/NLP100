# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient()
db = client.artist_database
collection = db.artist_collection

def top10_most_rating_artist(keyword='dance'):
    docs = collection.find({'tags.value' : keyword})
    docs.sort('rating.count', -1)

    for rank, doc in enumerate(docs):
        if rank < 10 and 'rating' in doc:
            print('{:20} {}'.format(doc['name'], doc['rating']['count']))

def main():
    top10_most_rating_artist()

if __name__ == '__main__':
    main()
