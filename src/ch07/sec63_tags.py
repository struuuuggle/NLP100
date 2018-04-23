# -*- coding: utf-8 -*-
import sys
import os
import json
import gzip
import redis
current_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(current_dir, "../../lib/artist.json.gz")


def create_db(filename):
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    with gzip.open(filename, 'r') as f:
        for line in f:
            json_dict = json.loads(line)
            try:
                artist = json_dict['name']
                original_tags = json_dict['tags']
            except KeyError:
                continue

            parsed_tags = {}
            for tag in original_tags:
                parsed_tags[tag['value']] = tag['count']
            r.set(artist, parsed_tags)


def search_tags(artist):
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    tags = r.get(artist).decode()
    return tags


def main():
    # コマンドライン引数でアーティスト名を受け取る
    # 空白も含めて読み込みたい場合は，single quoteでくくるか，'\ 'を使用する
    artist = sys.argv[1]
    try:
        create_db(data)
        print(search_tags(artist))
    except Exception:
        print("Redis server not found!\nBefore you run this script, the command below.\n")
        print("$ redis-server\n")


if __name__ == '__main__':
    main()
