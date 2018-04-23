# -*- coding: utf-8 -*-
import sys
import redis

def search_kvs(key):
    """
    アーティスト名(name)を受け取り，活動場所(area)を返す
    """
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    value = r.get(key)
    print(value.decode())

def main():
    # コマンドライン引数でアーティスト名を受け取る
    # 空白も含めて読み込みたい場合は，single quoteでくくるか，'\ 'を使用する
    artist_name = sys.argv[1]
    try:
        search_kvs(artist_name)
    except Exception:
        print("Redis server not found!\nBefore you run this script, the command below.\n\n$ redis-server\n")

if __name__ == '__main__':
    main()
