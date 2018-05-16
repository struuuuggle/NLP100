# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.artist_database
collection = db.artist_collection

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':

        # リクエストフォームから取得した「アーティスト名」
        keyword = request.form['name']

        # mongoDBからアーティスト名を<keyword>から検索
        docs = collection.find({'name' : keyword})
        docs.sort('rating.count', -1)

        return render_template('index.html', docs=docs)

    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
